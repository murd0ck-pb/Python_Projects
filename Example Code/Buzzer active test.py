#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BuzzerPin = 10    # pin10

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BuzzerPin, GPIO.OUT)
	GPIO.output(BuzzerPin, GPIO.LOW)

def loop():
	while True:
		GPIO.output(BuzzerPin, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(BuzzerPin, GPIO.LOW)
		time.sleep(0.5)

def destroy():
	GPIO.output(BuzzerPin, GPIO.LOW)
	GPIO.cleanup()                     # Release resource

while True:    # Program start from here
        setup()
        loop()

