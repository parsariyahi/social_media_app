from flask import Blueprint, redirect, url_for, request
from flask_login import login_required, current_user

from ..database.Models import Message
from .. import db

message = Blueprint('message', __name__)
""" 
:prefix /msg/<routes>
"""

@message.route('/send', methods=['GET', 'POST'])
@login_required
def send():
    """
    Send a message
    :methods GET, POST
    :return
        :redirect dashboard
    """
    if request.method == 'POST' and request.form.get('msg_send') :
        msg = {
            'from_node': current_user.username,
            'to_node': request.form.get('to_node'),
            'title': request.form.get('title'),
            'content': request.form.get('content'),
        }

        new_msg = Message(**msg)
        db.session.add(new_msg)
        db.session.commit()

    return redirect(url_for('dashboard.index'))

