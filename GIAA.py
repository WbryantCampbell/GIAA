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
	msg = options[b]()
	device.show_message(msg)	

options = {0: 'Thank You!',
			1: 'Go Around!',
			2: 'Left Lane is for Passing!',
			3: 'F*#$% Y&%$',}
	
if __name__ == '__main__' :

    device.show_message(sys.argv[0])
    main()

	

	
    
   
