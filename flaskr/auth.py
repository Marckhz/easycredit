import functools
import datetime
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/home', methods=('GET', 'POST'))
def home():

	if request.method == 'POST':
		username = request.form['username']
		db = get_db()
		error = None
				
		if not username:
			error = "required"
		elif db.execute(
			'SELECT id FROM user WHERE username = ?', (username,)
			).fetchone() is not None:
				error = 'user {} is already registerd'.format(username)

		if error is None:
			db.execute(
				'INSERT INTO user (username) VALUES (?)',
				(username,)
				)
			db.commit()
			return redirect(url_for('auth.register'))


	return render_template('auth/home.html')




@bp.route('/home', methods=('GET', 'POST'))
def login():
	if request.method == 'POST':
		username = request.form['username']
		db = get_db()
		error = None
		user = db.execute(
		'SELECT * FROM user WHERE username = ?', (username,)
		).fetchone()


		if user is None:
			error = "No user?"

		if error is None:
			session.clear()
			session['user_id'] = user['id']
			return redirect(url_for('auth.register'))

		flash(error)

	return render_template('auth/home.html')

@bp.route('/index', methods =('GET', 'POST'))
def register():
	
	if request.method =='POST':
		balance = request.form['balance']
		edad = request.form['edad']
		creditCard = request.form['checkbox']
		plazo = request.form['group1']
		db = get_db()

		error = None

		if error is None:
			db.execute(
				'INSERT INTO userinfo(balance, age ,creditCard, plazo) VALUES(?,?,?,?)',
				(balance, edad, creditCard, plazo)
				)
			db.commit()

	db =get_db()
	var = db.execute(
		'SELECT balance as primerblance, (balance * 0.05) + balance AS 3meses, (balance * 0.10) + balance AS 6meses FROM userinfo WHERE (plazo = 3 OR plazo = 6)').fetchall()


	

	return render_template('auth/index.html', var = var)

@bp.route('/index', methods = ('GET', 'POST'))
def vista1():

	error= None
	db = get_db()
	if error is None:
		
		data = db.execute(
			'SELECT fecha, plazo, balance, status FROM userinfo').fetchone()

	return render_template('auth/index.html', data=data)


@bp.route('/admin', methods=('GET', 'POST'))
def admin_login():

	if request.method == 'POST':
			
		username = request.form['username']
		db = get_db()
		error = None
		user = db.execute(
			'SELECT * FROM useradmin WHERE useradminame = ?',(username,)
			).fetchone()

		if user is None:
			error = "bro do you even admin?"

		if error is None:
			session.clear()
			session['user_id'] = user['id']
			return redirect(url_for('auth.dashboard'))
		
		flash(error)


	
	return render_template('auth/admin.html')


@bp.route('/dashboard', methods=('GET', 'POST'))
def dashboard():


	db = get_db()	
	data = db.execute('SELECT id, balance, age, creditCard, plazo, fecha  FROM userinfo').fetchall()





	return render_template('auth/dashboard.html', data = data)


#def get_update(id, check_user = True):






@bp.route('/dashboard', methods=('GET', 'POST'))
def update_table():



	if request.method =='POST':
		go = request.form['go']
		db = get_db()

		var = db.execute('UPDATE userinfo SET status = ?',(go)
			).fetchone()
		db.commit()


		

	return render_template('auth/dashboard.html')





	

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view