import os

from flask import Flask

from logging.config import dictConfig


def create_app(test_config=None):

	dictConfig({
	    'version': 1,
	    'formatters': {'default': {
	        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
	    }},
	    'handlers': {'wsgi': {
	        'class': 'logging.StreamHandler',
	        'stream': 'ext://flask.logging.wsgi_errors_stream',
	        'formatter': 'default'
	    }},
	    'root': {
	        'level': 'INFO',
	        'handlers': ['wsgi']
	    }
	})
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
	)

	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)



	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	from . import db
	db.init_app(app)

	from . import auth
	app.register_blueprint(auth.bp)

	from . import index
	app.register_blueprint(index.bp)
	app.add_url_rule('/', endpoint='index')


	from . import protected
	app.register_blueprint(protected.bp)

	from . import file_upload
	app.register_blueprint(file_upload.bp)

	from . import public
	app.register_blueprint(public.bp)

	from . import error_handling
	app.register_blueprint(error_handling.bp)




	return app;