from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin) :
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    full_name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    email = db.Column(db.String(150))
    phone_number = db.Column(db.String(150))
    bio = db.Column(db.Text)
    privacy_status = db.Column(db.Integer)
    password = db.Column(db.String(150))

    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model) :
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))
    title = db.Column(db.String(250))
    content = db.Column(db.Text)

class FriendRequest(db.Model) :
    __tablename__ = 'friend_requests'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))
    status = db.Column(db.Integer, default=0)


class Vertex(db.Model) :
    __tablename__ = 'vertices'

    id = db.Column(db.Integer, primary_key=True)
    from_node = db.Column(db.String(150))
    to_node = db.Column(db.String(150))
