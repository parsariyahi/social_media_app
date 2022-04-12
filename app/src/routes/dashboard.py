from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user


from ..database.Models import FriendRequest, Message, Vertex

dashboard = Blueprint('dashboard', __name__)
"""
prefix: /dash/<routes>
"""

@dashboard.route('/')
@login_required
def index() :

    """Geting the information that we need ro show in dashboard"""
    messages = Message.query.filter_by(to_node=current_user.username).all()
    requests = FriendRequest.query.filter_by(to_node=current_user.username).all()
    followers_count = Vertex.query.filter_by(to_node=current_user.username).count()
    followings_count = Vertex.query.filter_by(from_node=current_user.username).count()

    context = {
        'messages': messages,
        'requests': requests,
        'followers_count': followers_count,
        'followings_count': followings_count,
    }

    return render_template('dashboard/index.html', context=context)



@dashboard.route('/friends')
@login_required
def get_friends():
    context = {
        'followers': [],
        'followings': [],
    }
    followers = Vertex.query.filter_by(to_node=current_user.username).all()
    followings = Vertex.query.filter_by(from_node=current_user.username).all()

    for follower in followers:
        context['followers'].append([follower.from_node])

    for following in followings:
         context['followings'].append([following.to_node])

    return render_template('dashboard/friends.html', context=context)
