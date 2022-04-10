from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from ..database.Models import User
from .. import db


auth = Blueprint('auth', __name__)
""" 
prefix: /auth/<routes>
"""

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        user = {
                'username' : request.form.get('username', ''),
                'password' : request.form.get('password', ''),
        }

        user_db = User.query.filter_by(username=user['username']).first()
        if user_db :
            if check_password_hash(user_db.password, user['password']) :
                flash('Logged in successfully!', category='success')
                login_user(user_db, remember=True)
                #TODO this must send user to profile, something like views.profile
                return redirect(url_for('dashboard.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html")


@auth.route('/logout')
@login_required
def logout():
    """Logout user and
    send it to login page
    """
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' :
        new_user = {
                'username' : request.form.get('username', None),
                'full_name' : request.form.get('full_name', None),
                'email' : request.form.get('email', None),
                'phone_number' : request.form.get('phone_number', None),
                'age' : int(request.form.get('age', 0)),
                'bio' : request.form.get('bio', None),
                'privacy_status' : int(request.form.get('privacy_status', 0)),
                'password' : generate_password_hash(request.form.get('password', ''), method='sha256'), 
        }
        user = User.query.filter_by(username=new_user['username']).first()
        if user:
              flash('User already exists.', category='error')
        else:
              new_user = User(**new_user)
              db.session.add(new_user)
              db.session.commit()
              login_user(new_user, remember=True)
              flash('Account created!', category='success')

              return redirect(url_for('dashboard.index'))

    return render_template("register.html", user=current_user)
