#!/usr/bin/env python3
"""
    SocialMitux.helpers.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    Databases models using ´flask_sqlalchemy´.
    :copyright: © 2019 by Manuel Rubio.
"""
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(55), unique=True, nullable=False)
    email = db.Column(db.String(65), unique=True, nullable=False)
    biography = db.Column(db.String(999), nullable=True)
    registration_date = db.Column(db.DateTime, nullable=False,
        default=datetime.datetime.utcnow())
    password = db.Column(db.String(94), nullable=False)
    friends_id = db.Column(db.Integer, nullable=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.__hash_password(password)

    @staticmethod
    def __hash_password(password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.username!r}, email, password)')
