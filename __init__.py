#!/usr/bin/env python3
"""
    SocialMitux
    ~~~~~~~~~~~
    Simple social network for get learn
    :copyright: © 2019 by Manuel Rubio.
"""
#=====================
#: Importing modules
#=====================
from flask import (
    Flask, render_template,
    request, flash, redirect,
    url_for, session
)
from config import DevelopmentConfig
from helpers.forms import RegisterForm, LoginForm
from helpers.models import db, User


app = Flask(__name__)
app.config.from_object(DevelopmentConfig) # Environment: Development

#=============
#: Functions
#=============
def create_session(user_id, username):
    session['user_id'] = user_id
    session['username'] = username

#==============================
#: Routes and functionalities.
#==============================
@app.route('/', methods=['GET', 'POST'])
def index():
    """ Function in charge of administrate index page
        functionalities.
        :return: -> function:
            Returns a template HTML of index page.
    """
    return render_template('index.html')

@app.route('/users/register', methods=['GET', 'POST'])
def register_user():
    """ Function in charge of administrate registration page and
        validate the sign up users.
    """
    #: Creating `RegisterForm` instance for renderizate to view.
    register_form = RegisterForm(request.form)

    #: Validating if query request method is 'POST' and ´register_form´
    #: data is correct.
    if request.method == 'POST' and register_form.validate():
        #: Getting data.
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        #: Create user.
        new_user = User(username=username,
                        email=email,
                        password=password)
        #: Recording user.
        db.session.add(new_user)
        db.session.commit()
        #: Sending a message of success.
        flash('User registered successfully!')
        return redirect(url_for('index'))

    return render_template('users/register.html',
                            registerForm=register_form)

@app.route('/users/login', methods=['GET', 'POST'])
def login_user():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            create_session(user.id, user.username)
            flash('Hello %s' % user.username)
            return redirect(url_for('index'))
    return render_template('users/login.html', loginForm=login_form)


@app.route('/users/logout', methods=['GET'])
def logout_user():
    user_data = [
        'user_id',
        'username'
    ]
    for data in user_data:
        session.pop(data)
    return redirect(url_for('index'))
