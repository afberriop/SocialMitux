from flask import (
    Flask, render_template,
    request, flash,
)
from config import DevelopmentConfig
from helpers.forms import RegisterForm

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/users/register', methods=['GET', 'POST'])
def register_user():
    register_form = RegisterForm(request.form)
    return render_template('users/register.html',
                            registerForm=register_form)
