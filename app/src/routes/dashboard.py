from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/')
@login_required
def index() :
    return render_template('profile/index.html')


@dashboard.route('/test')
def test_dash():
    return {'some': 'akjdflkadjsf'}
