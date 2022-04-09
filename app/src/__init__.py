#from flask_sqlalchemy import SQLAlchemy

#from .database.db_oprations import Db
#from .objects.User import User
from .consts import CONSTS
from .database.Models import db, User, Message, FriendRequest, Vertex

from .routes.auth import auth
from .routes.message import message
from .routes.friend_request import friend_request
from .routes.dashboard import dashboard

#our db is here to be used everywhere
# db = SQLAlchemy()
