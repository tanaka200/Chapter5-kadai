#!/usr/bin/env python

import cgi
import cgitb    # display CGI error on browser
import time
import RPi.GPIO as GPIO

def setservo(angle):
    duty = angle / 18.0 + 2.0
    GPIO.output(2, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(2, False)
    servo.ChangeDutyCycle(0)

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web SERVO')

print('<form action="" method="post">')
print('<input type="text" name="servodeg" size="6">')
print('<input type="submit" value="SET">')
print('</form>')

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)     # PWM for servo
servo = GPIO.PWM(2, 50)
servo.start(0.0)

form = cgi.FieldStorage()
value = form.getvalue("servodeg")

if value is not None:
    try:
        angle = float(value)
        setservo(angle)
        print(f'Servo set to {angle} degrees.')
    except ValueError:
        print('Invalid input. Please enter a valid numerical value.')

GPIO.cleanup()
