from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin) :
    """
    user model

    :primary key: id
    :inherit db.Model, UserMixin
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    full_name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    privacy_status = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Message(db.Model) :
    """
    message model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150), nullable=False)
    to_node = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(250))
    content = db.Column(db.Text)

class FriendRequest(db.Model) :
    """
    friend request model

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'friend_requests'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150), nullable=False)
    to_node = db.Column(db.String(150), nullable=False)
    status = db.Column(db.Integer, default=0)


class Vertex(db.Model) :
    """
    graph model

    :from_node (username)
    :to_node (username)
    [from_node ---> to_node]
    [-|---------|---------|]
    [-V---------V---------V]
    [vertex1--edge--vertex2]

    :primary key: id
    :inherit db.Model
    """
    __tablename__ = 'vertices'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150), nullable=False)
    to_node = db.Column(db.String(150), nullable=False)
