#!/usr/bin/env python3
"""
    SocialMitux.helpers.forms
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    All formularies for renderizate to the view.
    :copyright: © 2019 by Manuel Rubio
"""
from wtforms import Form, StringField, PasswordField, validators
from wtforms.fields.html5 import EmailField


class RegisterForm(Form):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(max=55,
            message='Characters limit reached')
    ])
    email = EmailField('Email', [
        validators.DataRequired(),
        validators.Length(max=65,
            message='Characters limit reached')
    ])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.Length(min=8,
            message='Minimum 8 characters'),
        validators.EqualTo('confirm_password',
            message='Passwords not match')
    ])
    confirm_password = PasswordField('Confirm Password')
