import RPi.GPIO as GPIO

class Button:
    pins = range(0, 2)

    def __init__(self, pin1, pin2):
        self.pins[0] = pin1
        self.pins[1] = pin2

        GPIO.setup(self.pins[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pins[1], GPIO.IN, pull_up_down=GPIO.PUD_UP)


    def is_forward(self):
        return GPIO.input(self.pins[0])


    def is_backward(self):
        return GPIO.input(self.pins[1])
