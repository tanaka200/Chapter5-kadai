#!/usr/bin/env python

import cgi
import cgitb    #display CGI error on browser
import time
import RPi.GPIO as GPIO


print('Content-type: text/html; charset=UTF-8\r\n')
print('Web SERVO')

print('<form action="" method="post">')
print('<input type="text" name="servodeg" size="6">')
print('<input type="submit" value="SET">')
print('</form>')


GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)		#PWM for servo
servo = GPIO.PWM(2, 50)
servo.start(0.0)


form = cgi.FieldStorage()
value = form.getvalue("servodeg")

print(value) # for debug


GPIO.cleanup()

