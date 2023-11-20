#!/usr/bin/env python

from flask import Flask, render_template, request
import time
import RPi.GPIO as GPIO

app = Flask(__name__)

def setservo(angle):
    duty = angle / 18.0 + 2.0
    GPIO.output(2, True)
    servo.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(2, False)
    servo.ChangeDutyCycle(0)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            angle = float(request.form['servodeg'])
            setservo(angle)
            message = f'Servo set to {angle} degrees.'
        except ValueError:
            message = 'Invalid input. Please enter a valid numerical value.'
        return render_template('index.html', message=message)
    return render_template('index.html', message=None)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)  # PWM for servo
    servo = GPIO.PWM(2, 50)
    servo.start(0.0)

    GPIO.cleanup()
