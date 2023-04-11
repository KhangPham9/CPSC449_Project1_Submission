
from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(401)
def unauthorized(e):
	return render_template('unauthorized.html'), 401

@bp.app_errorhandler(403)
def unauthorized(e):
	return render_template('unauthorized.html'), 403


@bp.app_errorhandler(413)
def unauthorized(e):
	return render_template('too_large.html'), 413



@bp.app_errorhandler(415)
def unauthorized(e):
	return render_template('wrong_format.html'), 415