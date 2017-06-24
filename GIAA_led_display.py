#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import max7219.led as led
import sys

device = led.matrix(cascaded=4)
device.orientation(90)
	
def main() :
	
	a = sys.argv[1]
	b = int(a)
	msg = options[b]
	#device.show_message(msg)	
	print(msg)

options = {0: '',
			1: 'Go Around!',
			2: 'Left Lane is for Passing!',
			3: 'Learn to Drive!',
			4: 'Thank You!',}
	
if __name__ == '__main__' :

    #device.show_message(sys.argv[0])
    main()

	

	
    
   
