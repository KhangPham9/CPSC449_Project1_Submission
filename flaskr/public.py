from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, current_app
)

bp = Blueprint('public', __name__)


@bp.route('/public')
def public():
    return render_template('public.html')
