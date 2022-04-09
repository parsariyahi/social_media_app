from flask import Flask, render_template, request, session, redirect, url_for
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from src import (
        db, User, Message, FriendRequest, Vertex, CONSTS,
       auth, message, friend_request, dashboard, 
    )

app = Flask(__name__)
app.secret_key = CONSTS.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://prrh:parsa1981@localhost/pars_messenger'
db.init_app(app)

#db.drop_all(app=app)
#db.create_all(app=app)


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(message, url_prefix='/msg')
app.register_blueprint(friend_request, url_prefix='/req')
app.register_blueprint(dashboard, url_prefix='/dash')


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


if __name__ == "__main__" :
    app.debug = True
    app.run()
