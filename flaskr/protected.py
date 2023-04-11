from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)
from werkzeug.exceptions import abort

from flaskr.db import get_db

import jwt

bp = Blueprint('protected', __name__)


@bp.route('/protected')
def protected():

    token = request.cookies.get('token')
    current_app.logger.info(token)

    try:
        decoded_token = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        current_app.logger.info(decoded_token)
        return render_template('protected.html')

    except jwt.exceptions.InvalidTokenError:
        abort(401)

