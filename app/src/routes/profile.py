from flask import Blueprint, render_template, request, session, redirect, url_for
from flask_login import login_required, current_user

profile = Blueprint('some')

@profile.route('/')
@login_required
def profile() :
    return render_template('profile/index.html')
