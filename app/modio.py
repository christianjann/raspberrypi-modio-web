# -*- coding: utf-8 -*-
"""
    raspberrypi-modio-web
    ~~~~~~~~~~~~~~~~~~~~~

    A simple Python webapp to control something via Olimex's MOD-IO2

    :copyright: (c) 2013 by Christian Jann.
    :license: AGPL, see LICENSE for more details.
"""

import subprocess


def send_modio(data):
    try:
        subprocess.call(["i2c-tool", "-w", "0", "0x48", "4",
                         "0x02", "0xA0", "0x40", data])
    except OSError:
        print("ERR: i2c-tool not found")


class Modio:
    def __init__(self):
        send_modio("0x00")
        self.rel1 = 0
        self.rel2 = 0

    def relay1_on(self):
        if(self.rel2 == 1):
            send_modio("0x03")
        else:
            send_modio("0x01")

    def relay1_on(self):
        self.rel1 = 1
        if(self.rel2 == 1):
            send_modio("0x03")
        else:
            send_modio("0x01")

    def relay2_on(self):
        self.rel2 = 1
        if(self.rel1 == 1):
            send_modio("0x03")
        else:
            send_modio("0x02")

    def relay1_off(self):
        self.rel1 = 0
        if(self.rel2 == 1):
            send_modio("0x02")
        else:
            send_modio("0x00")

    def relay2_off(self):
        self.rel2 = 0
        if(self.rel1 == 1):
            send_modio("0x01")
        else:
            send_modio("0x00")
