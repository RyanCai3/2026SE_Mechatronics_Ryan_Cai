from servo import Servo
from machine import Pin, PWM
from PID_Controller import PIDControl
from PiicoDev_Unified import sleep_ms
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

# Creating A PWM Servo Controller
servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(20))

# Setting Parameters For The Servo
freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

# Creating Objects
my_servo = Servo(servo_pwm, min_us, max_us, dead_zone_us, freq)
my_servo2 = Servo(servo_pwm2, min_us, max_us, dead_zone_us, freq)
range_a = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
range_b = PiicoDev_Ultrasonic(id=[0, 0, 1, 0]) 

# Defining Movement Functions
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
    my_servo.set_duty(1340)
    my_servo2.set_duty(1340)

def turn_right():
    my_servo.set_duty(1635)
    my_servo2.set_duty(1635)

clearance = True

# Main Running
while clearance == True:
    forward()
    print(f"{range_a.distance_mm}, {range_b.distance_mm}")
    if range_a.distance_mm < 200:
        print("Obstacle Detected!")
        clearance = False

if range_b.distance.mm < 50:
    print("Obstacle On Right, Turning Left")
    turn_left()
    clearance = True
else:
    print("Turning Right")
    turn_right()
    clearance = True