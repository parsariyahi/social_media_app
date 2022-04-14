from flask import Blueprint, redirect, url_for, request
from flask_login import login_required, current_user

from ..database.Models import FriendRequest, Vertex
from .. import db

friend_request = Blueprint('friend_request', __name__)
""" 
:prefix /req/<routes>
"""

@friend_request.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    """
    Send a friend request,
    login is required.

    :methods GET, POST
    :return
        :redirect dashboard
    """
    if request.method == 'POST' :
        req = {
            'from_node': current_user.username,
            'to_node': request.form.get('to_node', ''),
        }
        new_req = FriendRequest(**req)
        db.session.add(new_req)
        db.session.commit()

    return redirect(url_for('dashboard.index'))


@friend_request.route('/accept', methods=['GET', 'POST'])
@login_required
def accept():
    """
    Accept a friend request,
    login is required.

    :methods GET, POST
    :return
        :redirect dashboard 
    """
    req = {
        'from_node': request.args.get('from_node', '')
    }

    """Change requests status,

    status = 0 : nothing happend
    status = 1 : accepted
    status = 2 : rejected
    """
    if req['from_node'] :
        req_db = FriendRequest.query.filter_by(from_node=req['from_node']).update({'status': 1}) #set status to 1
        db.session.commit()

        friend = Vertex(from_node=req['from_node'], to_node=current_user.username)
        db.session.add(friend)
        db.session.commit()

    return redirect(url_for('dashboard.index'))



@friend_request.route('/reject', methods=['GET', 'POST'])
@login_required
def reject():
    """
    Reject a friend request,
    login is required.

    :methods GET, POST
    :return
        :redirect dashboard
    """
    req = {
        'from_node': request.args.get('from_node', '')
    }

    """Change requests status,

    status = 0 : nothing happend
    status = 1 : accepted
    status = 2 : rejected
    """
    if req['from_node'] :
        req_db = FriendRequest.query.filter_by(from_node=req['from_node']).update({'status': 2}) #set status to 2
        db.session.commit()

    return redirect(url_for('dashboard.index'))
