from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user


from ..database.Models import User, FriendRequest, Message, Vertex
from .. import db

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index() :
    vertices = FriendRequest.query.filter_by(from_node=req['from_node'])
    messages = FriendRequest.query.filter_by(from_node=req['from_node'])
    requests = FriendRequest.query.filter_by(from_node=req['from_node'])
    return render_template('profile/index.html')
