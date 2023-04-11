import functools

from flask import (
	Blueprint, abort, flash, g, redirect, render_template, request, session, url_for, jsonify
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

from flask import current_app


import jwt

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		db = get_db()

		error = None

		if not username:
			error = 'Username is required.'
		elif not password:
			error = 'Password is required.'


		if error is None:
			# perform registration activities here

			try: 
				db.cur.execute(
					'INSERT INTO user (username, password) VALUES (%s, %s)',
					(username, generate_password_hash(password))
				)
				db.commit()
			except db.IntegrityError:
				error = f'User {username} is already registered.'
			else:
				return redirect(url_for("auth.login"))

			flash(error)

	return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		db = get_db()
		error = None

		db.cur.execute(
			'SELECT * FROM user WHERE username = %s',
			(username)
		)
		user = db.cur.fetchone()
		# current_app.logger.info(user['password'])

		if user is None:
			error = 'Incorrect username.'
			abort(403)

		elif not check_password_hash(user['password'], password):
			error = 'Incorrect password'
			abort(403)

		if error is None:
			session.clear()
			session['user_id'] = user['id']
			session['loggedin'] = True

			token = jwt.encode({"user": user}, current_app.config['SECRET_KEY'])
			# current_app.logger.info(token)
			res = redirect(url_for('index'))

			res.set_cookie('token', token) 
			# current_app.logger.info(res)

			return res

		flash(error)

	return render_template('auth/login.html')




@bp.route('/logout', methods=('GET', 'POST'))
def logout():
	session.clear()


	res = redirect(url_for('index'))
	res.set_cookie('token', '', expires=0)
	return res

