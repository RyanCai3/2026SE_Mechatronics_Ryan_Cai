from servo import Servo
from machine import Pin, PWM
from PID_Controller import PIDControl
from PiicoDev_Unified import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

class MovementSubsystem:
    def __init__(self, wheel_1, wheel_2):
        self.__wheel_1 = wheel_1
        self.__wheel_2 = wheel_2

    def stop(self):
        wheel_1.set_duty(2000)
        wheel_2.set_duty(1000)

    def move_forward(self):
        wheel_1.set_duty(2000)
        wheel_2.set_duty(1000)

    def move_backward(self):
        wheel_1.set_duty(1000)
        wheel_2.set_duty(2000)

    def turn_left(self):
        wheel_1.set_duty(1335)
        wheel_2.set_duty(1335)
    
    def turn_right(self):
        wheel_1.set_duty(1630)
        wheel_2.set_duty(1630)

servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(20))
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500
wheel_1 = Servo(servo_pwm, min_us, max_us, dead_zone_us, freq)
wheel_2 = Servo(servo_pwm2, min_us, max_us, dead_zone_us, freq)