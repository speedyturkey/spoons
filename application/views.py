from application import application, models
from flask import render_template


@application.route('/')
def index():
    requests = models.Requests.query.all()
    return render_template('index.html',
    title='Home',
    logged_in=1,
    first_name='Wilward',
    last_name='McNunes',
    requests=requests)

@application.route('/orders')
def orders():
    return render_template('orders_all.html', title='Orders', logged_in=0, first_name='Wilward', last_name='McNunes')

@application.route('/requests')
def requests():
    return render_template('requests_all.html', title='Requests', logged_in=1, first_name='Wilward', last_name='McNunes')

@application.route('/users')
def users():
    return render_template('users.html', title='Users', logged_in=1, first_name='Wilward', last_name='McNunes')
