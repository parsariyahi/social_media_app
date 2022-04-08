from flask import Blueprint, redirect, url_for, request
from flask_login import login_required

from ..database.Models import FriendRequest
from .. import db

friend_request = Blueprint('friend_request', __name__)

@friend_request.route('/send', methods=['GET', 'POST'])
@login_required
def friend_request_send():
    if request.method == 'POST' :
        req = {
            'from_node': request.form.get('from_node'),
            'to_node': request.form.get('to_node'),
        }

        new_req = FriendRequest(**req)
        db.session.add(new_req)
        db.session.commit()

        return redirect(url_for('profile.profile'))
