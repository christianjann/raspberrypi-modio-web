#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    raspberrypi-modio-web
    ~~~~~~~~~~~~~~~~~~~~~

    A simple Python webapp to control something via Olimex's MOD-IO2

    :copyright: (c) 2013 by Christian Jann.
    :license: AGPL, see LICENSE for more details.
"""

from app.settings import settings
from app.app import app

if __name__ == '__main__':

    # '0.0.0.0': listen on all public IPs
    app.run(host='0.0.0.0', port=8080, debug=settings['debug'])
