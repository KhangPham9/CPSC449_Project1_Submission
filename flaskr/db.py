import pymysql
from flask_cors import CORS
import re
# from datetime import timedelta 

from flask import current_app, g
import click


def get_db():
	if 'db' not in g:
		g.db = pymysql.connect(
			host='localhost',
			user='khang',
			password='school',
			db='449_project1_db',
			cursorclass=pymysql.cursors.DictCursor
		)
		g.db.cur = g.db.cursor()

	return g.db



def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()



def init_db():
	db = get_db()
	sql_db_init = 'CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL);'
	db.cur.execute(sql_db_init)
	db.commit()



@click.command('init-db')
def init_db_command():
	init_db()
	click.echo('Initialized the database')



def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)


		