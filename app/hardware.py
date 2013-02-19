# -*- coding: utf-8 -*-
"""
    raspberrypi-modio-web
    ~~~~~~~~~~~~~~~~~~~~~

    A simple Python webapp to control something via Olimex's MOD-IO2

    :copyright: (c) 2013 by Christian Jann.
    :license: AGPL, see LICENSE for more details.
"""

import os
import subprocess
from flask import Blueprint, Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, Markup, escape, send_from_directory
from modio import Modio
from gpios import *

hardware = Blueprint('hardware', __name__)

# init gpio's
export_pins(23)
setpindirection(23, "out")
export_pins(24)
setpindirection(24, "out")

mymodio = Modio()


@hardware.route('/')
def control():
    in_out = {'gpio23': bool(readpins(23)),
              'gpio24': bool(readpins(24)),
              'relay1': bool(mymodio.rel1),
              'relay2': bool(mymodio.rel2)}
    return render_template('control.j2', in_out=in_out)


@hardware.route('/set_gpio', methods=('GET', 'POST',))
def set_gpio():
    if request.method == 'POST':
        if not session.get('logged_in'):
            flash('You need to log in!', 'error')
            return redirect(url_for('.control'))
        gpio23 = bool(request.form.get('gpio23'))
        gpio24 = bool(request.form.get('gpio24'))
        print("gpio23: ", gpio23)
        print("gpio24: ", gpio24)
        flash('GPIOs have been updated: GPIO23="' + str(gpio23)
              + '", GPIO24="' + str(gpio24) + '"', 'success')
        writepins(23, int(gpio23))
        writepins(24, int(gpio24))
    return redirect(url_for('.control'))


@hardware.route('/modio', methods=('GET', 'POST',))
def modio():
    if request.method == 'POST':
        if not session.get('logged_in'):
            flash('You need to log in!', 'error')
            return redirect(url_for('.control'))
        relay1 = bool(request.form.get('relay1'))
        relay2 = bool(request.form.get('relay2'))
        print("relay1: ", relay1)
        print("relay2: ", relay2)
        flash('RELAYs have been updated: RELAY1="' + str(relay1)
              + '", RELAY2="' + str(relay2) + '"', 'success')
        if(relay1):
            mymodio.relay1_on()
        else:
            mymodio.relay1_off()
        if(relay2):
            mymodio.relay2_on()
        else:
            mymodio.relay2_off()
    return redirect(url_for('.control'))


@hardware.route('/webcam')
def webcam():
    return render_template('webcam.j2')


@hardware.route('/webcam.jpeg')
def camimage():
    print('Acquiring image file....')
    # this may wear out your SD card because
    # each time the page gets reloaded
    # a new image will be stored on your SD card
    try:
        subprocess.call(['fswebcam', '-r', '640x480', '-d', '/dev/video0',
                        '--title=Raspberry Pi Webcam', '--subtitle=www.jann.cc',
                        os.path.join(hardware.root_path, '../data/webcam.jpg')])
    except OSError:
        print("ERR: fswebcam not found, please install fswebcam")
    return send_from_directory(os.path.join(hardware.root_path, '../data'),
                               'webcam.jpg', mimetype='image/jpeg')
