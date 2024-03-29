import time
import RPi.GPIO as GPIO

class Motor:
    wait_time = 0.0013

    sequence = range(0, 8)
    sequence[0] = [1,0,0,0]
    sequence[1] = [1,1,0,0]
    sequence[2] = [0,1,0,0]
    sequence[3] = [0,1,1,0]
    sequence[4] = [0,0,1,0]
    sequence[5] = [0,0,1,1]
    sequence[6] = [0,0,0,1]
    sequence[7] = [1,0,0,1]


    def __init__(self, pin1, pin2, pin3, pin4):
        self.pins = range(0, 4)
        self.pins[0] = pin1
        self.pins[1] = pin2
        self.pins[2] = pin3
        self.pins[3] = pin4

        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)

        self.reset()


    def reset(self):
        for pin in self.pins:
            GPIO.output(pin, False)


    def forward(self, steps):
        step_counter = 0
        for step in range(0, (steps*8)):
            for pin in range(0, 4):
                output_pin = self.pins[pin]

                if self.sequence[step_counter][pin] != 0:
                    GPIO.output(output_pin, True)
                else:
                    GPIO.output(output_pin, False)

            step_counter += 1

            if step_counter == 8:
                step_counter = 0
            
            if step_counter < 0:
                step_counter = 8

            time.sleep(self.wait_time)
            self.reset()


    def backward(self, steps):
        step_counter = 7
        for step in range(0, (steps*8)):
            for pin in range(0, 4):
                output_pin = self.pins[pin]

                if self.sequence[step_counter][pin] != 0:
                    GPIO.output(output_pin, True)
                else:
                    GPIO.output(output_pin, False)

            step_counter -= 1

            if step_counter == 0:
                step_counter = 7

            if step_counter < 0:
                step_counter = 7

            time.sleep(self.wait_time)
            self.reset()
