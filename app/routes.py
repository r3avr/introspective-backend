from flask import Blueprint, request, redirect, url_for, render_template, flash
from werkzeug.security import check_password_hash
from app.models import User

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
        # You can implement a session or just flash a message for now
        flash("Login successful", "success")
        return redirect(url_for('main.index'))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for('main.index'))
