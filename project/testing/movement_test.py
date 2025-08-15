import time
from machine import Pin, PWM
from servo import Servo

# create a PWM servo controller
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(20))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# create a servo object
my_servo = Servo(pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)
my_servo2 = Servo(pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq)

# Defining movement functions
def stop():
    my_servo.set_duty(1500)
    my_servo2.set_duty(1500)

def forward():
    my_servo.set_duty(2000)
    my_servo2.set_duty(1000)

def backward():
    my_servo.set_duty(1000)
    my_servo2.set_duty(2000)

def turn_left():
    my_servo.set_duty(1335)
    my_servo2.set_duty(1335)

def turn_right():
    my_servo.set_duty(1650)
    my_servo2.set_duty(1650)

# unit testing
while True:
    forward()
    print("Moving Forward")
    time.sleep(2)

    stop()
    print("Stopped")
    time.sleep(2)

    backward()
    print("Moving Backward")
    time.sleep(2)

    stop()
    print("Stopped")
    time.sleep(2)

    turn_left()
    print("Turning Left")
    time.sleep(2)

    stop()
    print("Stopped")
    time.sleep(2)

    turn_right()
    print("Turning Right")
    time.sleep(2)

    stop()
    print("Stopped")
    time.sleep(2)