# -*- coding: utf-8 -*-
"""
    raspberrypi-modio-web
    ~~~~~~~~~~~~~~~~~~~~~

    A simple Python webapp to control something via Olimex's MOD-IO2

    :copyright: (c) 2013 by Christian Jann.
    :license: AGPL, see LICENSE for more details.
"""

from werkzeug import check_password_hash, generate_password_hash
from settings import settings
import yaml
import os

def get_user(key,value):
    yamlfile=open(settings['datadir']+ 'users.yaml',"r")
    userconf = yaml.load(yamlfile)
    for user in userconf['users']:
        if (user[key]==value):
            return user
    return None

def add_user(username, password, email):
    if (get_user('username', username) is None):
    # check if the username is allready taken
        yamlfile=open(settings['datadir']+ 'users.yaml',"r")
        userconf = yaml.load(yamlfile)
        # userid = len(userconf['users']) +1
        userid = int(userconf['usercount'])
        userconf['usercount'] = userid + 1
        print(" * Adding user: " + username + " user_id=" + str(userid))
        yamlfile=open(settings['datadir']+ 'users.yaml',"w")
        userconf['users'].append({'username': username,
                                  'password_hash': generate_password_hash(password),
                                  'email': email,
                                  'user_id': userid})
        yaml.dump(userconf, yamlfile, default_flow_style=False)
        yamlfile.close()
    else:
        print(" * Error: username " + username + " already taken")
