from flask import Blueprint, render_template
from flask_login import login_required, current_user

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def home():
    return "<h1>FlaskTasker is alive!</h1>"

# TODO: proof of login for the time being.. This route should be moved to a different spot later when the user's module is implemented
@index_bp.route('/profile')
@login_required
def profile():
    return render_template('/profile.html', user=current_user)