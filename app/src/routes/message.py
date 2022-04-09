from flask import Blueprint, redirect, url_for, request
from flask_login import login_required

from ..database.Models import Message
from .. import db

message = Blueprint('message', __name__)


@message.route('/send', methods=['GET', 'POST'])
@login_required
def send_msg():
    if request.method == 'POST' :
        msg = {
            'from_node': request.form.get('from'),
            'to_node': request.form.get('to'),
            'title': request.form.get('title'),
            'content': request.form.get('content'),
        }

        new_msg = Message(**msg)
        db.session.add(new_msg)
        db.session.commit()
        return redirect(url_for('profile.profile'))




@message.route('/test')
def test_msg():
    return {'some': 'message'}
