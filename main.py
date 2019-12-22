#!/usr/bin/env python

# import required libs
import time
import RPi.GPIO as GPIO
from motor import Motor
from button import Button

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# be sure you are setting pins accordingly
# GPIO10,GPIO9,GPIO11,GPI25
# StepPins = [17,18,27,22]

motor1 = Motor(18, 17, 27, 22)
motor2 = Motor(12, 13, 19, 26)


# Start main loop
button = Button(14, 15)
while True:
    if button.is_forward():
        print("forward")
        motor1.forward(128)
        time.sleep(1)
        motor2.forward(128)
    elif button.is_backward():
        print("backward")
        motor1.backward(128)
        time.sleep(1)
        motor2.backward(128)
    else:
        motor1.reset()
        motor2.reset()

try:
    print("Started")
except:
  print("Failed")
finally:
    #cleaning up and setting pins to low again (motors can get hot if you wont)
    motor1.reset()
    motor2.reset()
    GPIO.cleanup()
