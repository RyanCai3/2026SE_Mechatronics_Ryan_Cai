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

while True:

# Left = 1340
# Right = 1630

    my_servo.set_duty(1340)
    my_servo2.set_duty(1340)
    time.sleep(2)

    my_servo.stop()
    my_servo2.stop()
    time.sleep(5)