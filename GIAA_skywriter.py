#!/usr/bin/env python

import skywriter
import signal
from os import system
import time

msg_to_send = 0
is_running = True

while is_running :

	@skywriter.flick()
	def flick(start,finish):
	  if(start == "north" and finish == "south"):
		print "Down!"
		system("sudo python2 /home/pi/GIAA/GIAA/GIAA_led_display.py 2")
	  elif(start == "south" and finish == "north"):
		print "Up!"
		system("sudo python2 /home/pi/GIAA/GIAA/GIAA_led_display.py 4")
	  elif(start == "west" and finish == "east"):
		print "Right!"
		system("sudo python2 /home/pi/GIAA/GIAA/GIAA_led_display.py 1")
	  elif(start == "east" and finish == "west"):
		print "Left"
		system("sudo python2 /home/pi/GIAA/GIAA/GIAA_led_display.py 2")
	  else:
		print ""
