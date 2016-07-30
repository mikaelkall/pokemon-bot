#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Pokemon Go bot.

This bot will catch them all.

"""

from ConfigParser import SafeConfigParser
from polib.polib import *

import datetime
import time
import sys
import os
import signal
import random

__author__ = 'Mikael Kall'
__email__ = 'kall.micke@gmail.com'

"""Setup signal to close program nicely"""
def signal_handler(signal, frame):
    print "\nYou pressed Ctrl+C!"
    os._exit(0)

signal.signal(signal.SIGINT, signal_handler)


class Go:

    def __init__(self):
        pass

    def banner(self):
        banner = """
 _____     _                        _____     
|  _  |___| |_ ___ _____ ___ ___   |   __|___ 
|   __| . | '_| -_|     | . |   |  |  |  | . |
|__|  |___|_,_|___|_|_|_|___|_|_|  |_____|___|
	"""
	print("%s%s" % ( "\033[91m", banner ))
	print("%s%s" % ( "\033[92m", "Mikael Kall [kall.micke@gmail.com]"))

    def print_usage(self):
	self.banner()
        print ("""\033[93m
Usage: go.py <OPTIONS> 

General Options

    pokestops	Spin pokestops
    pokemons	Hunt pokemons
    profile	View profile
    inventory	View inventory

	""")	


if __name__ == '__main__':

    if len(sys.argv)<2:
        Go().print_usage()
	sys.exit(0)

    opt = sys.argv[1].strip()

    if opt.lower() == "pokestops":
	print ("\033[93m")
	Polib().pokestops()
    elif opt.lower() == "pokemons":
	print ("\033[93m")
        Polib().pokemons()
    elif opt.lower() == "profile":
	print ("\033[93m")
	Polib().get_profile()
    elif opt.lower() == "inventory":
        print ("\033[93m")
        Polib().get_inventory()
    else:
	Go().print_usage()
