from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from src.routes import auth, message, friend_request, dashboard
from src.database import User, FriendRequest, Vertex, Message
from src.consts import SECRET_KEY, SQLALCHEMY_DATABASE_URI
from src import db

app = Flask(__name__)
app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
db.init_app(app)

""" for the first time,
uncomment these lines,
to create the database tables
"""
#db.drop_all(app=app)
#db.create_all(app=app)


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(message, url_prefix='/msg')
app.register_blueprint(friend_request, url_prefix='/req')
app.register_blueprint(dashboard, url_prefix='/dash')


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@app.route('/')
def index():
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


if __name__ == "__main__" :
    app.debug = True
    app.run()
