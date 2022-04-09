from flask import Blueprint, redirect, url_for, request
from flask_login import login_required, current_user

from ..database.Models import FriendRequest
from .. import db

friend_request = Blueprint('friend_request', __name__)

@friend_request.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    """Send a friend request to someone,

    only logged in users

    methods: GET, POST
    """
    if request.method == 'POST' :
        req = {
            'from_node': request.form.get('from_node', ''),
            'to_node': request.form.get('to_node', ''),
        }
        new_req = FriendRequest(**req)
        db.session.add(new_req)
        db.session.commit()

        return redirect(url_for('profile.profile'))


@friend_request.route('/accept', methods=['GET', 'POST'])
@login_required
def accept():
    """Accept a friend request,

    only logged in users

    methods: GET, POST
    """
    if request.method == 'POST':
        req = {
            'from_node': request.form.get('from_node', '')
        }

        """Change requests status,

        status = 0 : nothing happend
        status = 1 : accepted
        status = 2 : rejected
        """
        req_db = FriendRequest.query.filter_by(from_node=req['from_node']).update({'status': 1})
        db.session.commit()

        return redirect(url_for('profile.profile'))

    return redirect(url_for('profile.profile'))



@friend_request.route('/reject', methods=['GET', 'POST'])
@login_required
def reject():
    """Reject a friend request,

    only logged in users

    methods: GET, POST
    """
    if request.method == 'POST':
        req = {
            'from_node': request.form.get('from_node', '')
        }

        """Change requests status,

        status = 0 : in process
        status = 1 : accepted
        status = 2 : rejected
        """
        req_db = FriendRequest.query.filter_by(from_node=req['from_node']).update({'status': 2})
        db.session.commit()

        return redirect(url_for('profile.profile'))

    return redirect(url_for('profile.profile'))
