#!/usr/bin/env python
"""
    SocialMitux.config
    ~~~~~~~~~~~~~~~~~~
    App configuration attributes.
    :copyright: © 2019 by Manuel Rubio.
"""

#=====================================
# Importing modules for internal use.
#=====================================
import string as _string
import time as _time
import random as _random

#=====================
# Internal functions.
#=====================
def _generate_secret_key(limit):
    if not isinstance(limit, int): limit = 99

    secret_key = str()
    for i in range(limit):
        secret_key += _random.choice(_string.ascii_letters)
        secret_key += str(_random.randint(0, limit))

    return secret_key

#=======================
# Configuration classes.
#=======================
class BaseConfig:
    SECRET_KEY = ''
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    SECRET_KEY = _generate_secret_key(99)
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = ''
    #SQLALCHEMY_TRACK_MODIFICATIONS = False
