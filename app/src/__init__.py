from flask_sqlalchemy import SQLAlchemy

#from .database.db_oprations import Db
#from .objects.User import User
from .consts import CONSTS
from .database.Models import User, Message, FriendRequest, Vertex

from .routes.auth import auth
from .routes.message import message
from .routes.request import friend_request
from .routes.profile import profile

#our db is here to be used everywhere
db = SQLAlchemy()
