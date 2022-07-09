from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify
)

from Source.Application.Services.AuthService import *

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', None)
        password = request.form.get('password', None)

        AuthServiceInstance = AuthService();
        return AuthServiceInstance.tryLogin(username, password)
    else:
        return show_the_login_form()


def show_the_login_form():
    return render_template('auth/index.html', name=__name__)