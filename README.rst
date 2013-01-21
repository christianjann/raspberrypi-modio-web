
Raspberry Pi MOD-IO Web
=======================

A simple Python webapp to control something
via Olimex's MOD-IO2.

What you will need
------------------

- A Raspberry Pi: http://www.raspberrypi.org/
- Olimex's RPi-UEXT: https://www.olimex.com/Products/Modules/Adapters/RPi-UEXT/
- Olimex's MOD-IO2: https://www.olimex.com/Products/Modules/IO/MOD-IO2/
- A 26-PIN RIBBON CABLE: https://www.olimex.com/Products/Components/Cables/CABLE-IDC26-15cm/
- A webcam if you like

But you can also test this app on your PC if `Python <http://python.org/>`_ and
`Flask <http://flask.pocoo.org/>`_ are installed, on Arch Linux you would install
them by running::

  pacman -S python2 python2-flask python2-yaml

On Raspbian::

  sudo apt-get install python-flask python-yaml

To view live images from your webcam you will also need
`fswebcam <https://github.com/fsphil/fswebcam>`_.

How do I use it?
----------------

Just run the ``run.py`` file with your
python interpreter and the application will
greet you on http://localhost:8080/.

Log in with ``admin``, ``default``.

Please take a look at `my blog post
<http://www.jann.cc/2013/01/21/control_your_light_at_home_with_a_raspberry_pi.html>`_
for more information. This should be a good starting point for your own project.

I've also written a simpler app for for the
`iMX233-OLinuXino-MICRO <https://www.olimex.com/Products/OLinuXino/iMX233/iMX233-OLinuXino-MICRO/>`_
which consists of three files only, have a look
`here <https://github.com/christianjann/olinuxino-webcontrol-minimal>`_.
