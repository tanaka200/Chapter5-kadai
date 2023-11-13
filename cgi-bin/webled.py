#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web LED')

print('<form action="" method="post">')
print('<input type="submit" name="led" value="ON">')
print('<input type="submit" name="led" value="OFF">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

form = cgi.FieldStorage()
value = form.getvalue("led")

if value == 'ON':
	GPIO.output(14, GPIO.HIGH)
	print('LED ON')

elif value == 'OFF':
	GPIO.output(14, GPIO.LOW)
	print('LED OFF')


