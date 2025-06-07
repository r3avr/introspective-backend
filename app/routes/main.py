from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.models import User
from app import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        flash('Logged in successfully.', 'success')
        return redirect(url_for('main.dashboard'))
    else:
        flash('Invalid username or password.', 'error')
        return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))

@main.route('/manage/users')
@login_required
def manage_users():
    users = User.query.all()
    return render_template('manage_users.html', users=users)

@main.route('/manage/users/create', methods=['POST'])
@login_required
def create_user():
    username = request.form['username']
    password = request.form['password']

    if User.query.filter_by(username=username).first():
        flash('Username already exists.', 'error')
        return redirect(url_for('main.manage_users'))

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    flash('User created successfully.', 'success')
    return redirect(url_for('main.manage_users'))

@main.route('/manage/users/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    # Prevent deleting yourself
    if user.id == current_user.id:
        flash('You cannot delete your own account.', 'error')
        return redirect(url_for('main.manage_users'))

    db.session.delete(user)
    db.session.commit()

    flash(f'User "{user.username}" has been deleted.', 'success')
    return redirect(url_for('main.manage_users'))
