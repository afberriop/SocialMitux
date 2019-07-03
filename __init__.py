from flask import (
    Flask, render_template,
    request, flash, redirect,
    url_for
)
from config import DevelopmentConfig
from helpers.forms import RegisterForm
from helpers.models import db, User

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['GET', 'POST'])
def register_user():
    register_form = RegisterForm(request.form)
    if request.method == 'POST' and register_form.validate():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data
        new_user = User(username=username,
                        email=email,
                        password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('User registered successfully!')
        return redirect(url_for('index'))

    return render_template('users/register.html',
                            registerForm=register_form)
