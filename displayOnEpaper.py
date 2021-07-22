#!/usr/bin/python

import sys
import os
# picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
		sys.path.append(libdir)

import logging
import epd2in13bc
import time
from PIL import Image
import numpy as np
import traceback


logging.basicConfig(level=logging.INFO)

try:
	logging.info("DiplayDemo Demo")

	epd = epd2in13bc.EPD()
	logging.info("init and Clear")
	epd.init()
	epd.Clear()

	HBlackimage = Image.new('1', (epd.height, epd.width), 255)

	img = Image.open('out.jpg').resize((212, 104))
	
	epd.display(epd.getbuffer(img))

except IOError as e:
	logging.info(e)

except KeyboardInterrupt:
	logging.info("ctrl + c:")
	epd2in13bc.epdconfig.module_exit()
	exit()
