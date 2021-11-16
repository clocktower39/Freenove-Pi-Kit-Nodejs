import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Define output pins
pin_a = 32
pin_b = 36
pin_c = 38
pin_d = 40

GPIO.setup(pin_a, GPIO.OUT)
GPIO.setup(pin_b, GPIO.OUT)
GPIO.setup(pin_c, GPIO.OUT)
GPIO.setup(pin_d, GPIO.OUT)

# Set pins to low
GPIO.output(pin_a, GPIO.LOW)
GPIO.output(pin_b, GPIO.LOW)
GPIO.output(pin_c, GPIO.LOW)
GPIO.output(pin_d, GPIO.LOW)

# Define stepper motor step counting and max steps when stop
number_of_steps = 1
max_steps = 1000

# Rotate in clockwise direction, full step drive
# step    1  2  3  4
#         ----------
# pin_a   1  1  0  0
# pin_b   0  1  1  0
# pin_c   0  0  1  1
# pin_d   1  0  0  1

while True:

    #step 1
    GPIO.output(pin_a, GPIO.HIGH)
    GPIO.output(pin_b, GPIO.LOW)
    GPIO.output(pin_c, GPIO.LOW)
    GPIO.output(pin_d, GPIO.HIGH)
    time.sleep(0.002)

    #step 2
    GPIO.output(pin_a, GPIO.HIGH)
    GPIO.output(pin_b, GPIO.HIGH)
    GPIO.output(pin_c, GPIO.LOW)
    GPIO.output(pin_d, GPIO.LOW)
    time.sleep(0.002)

    #step 3
    GPIO.output(pin_a, GPIO.LOW)
    GPIO.output(pin_b, GPIO.HIGH)
    GPIO.output(pin_c, GPIO.HIGH)
    GPIO.output(pin_d, GPIO.LOW)
    time.sleep(0.002)

    #step 4
    GPIO.output(pin_a, GPIO.LOW)
    GPIO.output(pin_b, GPIO.LOW)
    GPIO.output(pin_c, GPIO.HIGH)
    GPIO.output(pin_d, GPIO.HIGH)
    time.sleep(0.002)

    # Calculate steps of stepper motor
    number_of_steps += 1

    if number_of_steps == max_steps:
        GPIO.output(pin_a, GPIO.LOW)
        GPIO.output(pin_b, GPIO.LOW)
        GPIO.output(pin_c, GPIO.LOW)
        GPIO.output(pin_d, GPIO.LOW)
        break
