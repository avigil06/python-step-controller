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

motor1 = Motor(17, 18, 27, 22)


# Start main loop
button = Button(15, 17)
try:
  while True:
    if button.is_forward():
        motor1.forward(100)
    elif button.is_backward():
        motor1.backward(100)
    else:
        motor1.reset()
    time.sleep(0.5)

except:
  print("Failed")
finally:
    #cleaning up and setting pins to low again (motors can get hot if you wont)
    motor1.reset()
    GPIO.cleanup()
