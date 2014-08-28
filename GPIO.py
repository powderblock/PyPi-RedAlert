import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(14, gpio.OUT)

on = False

def lightHandle():
        if on is True:
                gpio.output(14, gpio.HIGH)

        if on is False:
                gpio.output(14, gpio.LOW)

while True:
        math = raw_input()
        math = math.lower()
        if math == 'on':
