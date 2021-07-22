#!/usr/bin/python

import sys
import os
# picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
		sys.path.append(libdir)

import logging
import epd2in13bc
from PIL import Image
from io import BytesIO
from picamera import PiCamera
from time import gmtime, strftime, sleep


logging.basicConfig(level=logging.INFO)

try:
	logging.info("DiplayDemo Demo")

	imageName = strftime("%Y-%m-%d-%H-%M-%S", gmtime()) + ".jpg"
	
	stream = BytesIO()
	camera = PiCamera(resolution=(212, 104), framerate=30)
	camera.iso = 1000
	camera.start_preview()
	sleep(2)
	camera.capture(stream, format='jpeg')
	camera.capture(imageName)
	camera.stop_preview()
	stream.seek(0)

	epd = epd2in13bc.EPD()
	logging.info("init and Clear")
	epd.init()
	epd.Clear()

	HBlackimage = Image.new('1', (epd.height, epd.width), 255)
	
	img = Image.open(stream)

	# img = Image.open('out.jpg').resize((212, 104))
	
	epd.display(epd.getbuffer(img))

except IOError as e:
	logging.info(e)

except KeyboardInterrupt:
	logging.info("ctrl + c:")
	epd2in13bc.epdconfig.module_exit()
	exit()
