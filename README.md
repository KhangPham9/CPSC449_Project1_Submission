# CPSC 449 Midterm Project
- Name: Khang Pham
- Email: khangpham9999@csu.fullerton.edu


# Python dependancies

Package            Version
------------------ -------
cffi               1.15.1 
click              8.1.3  
cryptography       40.0.1 
Flask              2.2.3  
Flask-Cors         3.0.10 
importlib-metadata 6.1.0  
itsdangerous       2.1.2  
Jinja2             3.1.2  
MarkupSafe         2.1.2  
pip                20.0.2 
pkg-resources      0.0.0  
pycparser          2.21   
PyJWT              2.6.0  
PyMySQL            1.0.2  
setuptools         44.0.0 
six                1.16.0 
Werkzeug           2.2.3  
zipp               3.15.0 

# Setup
	The python dependancies should already be installed
	in the venv folder. To source the dependancies, 
	in the root of the repository, run the command:
		source venv/bin/activate

	To setup the database, you will have to use mysql
	and you will have to change the host, user, password,
	and database on lines 13-16 of db.py. This is
	just necessary so that the database connection will be made.
	Then you will have to create the user table which you
	can find the sql for on line 35 of db.py. 


# How to run
	To start up the app, in the root of the repository,
	run the command:
		flask --app flaskr run --debug 