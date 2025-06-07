from flask import request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash
from app.models import User
from app.routes import main
from app.models import db

@main.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        flash('Logged in successfully.', 'success')
        return redirect(url_for('main.dashboard'))
    else:
        flash('Invalid username or password.', 'error')
        return redirect(url_for('main.index'))

@main.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in first.', 'error')
        return redirect(url_for('main.index'))
    return render_template('dashboard.html')
