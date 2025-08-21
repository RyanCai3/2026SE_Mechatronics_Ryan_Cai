from servo import Servo
from machine import Pin, PWM
from PiicoDev_Unified import sleep_ms
from controller import MovementSubsystem

servo_pwm = PWM(Pin(16))
servo_pwm2 = PWM(Pin(20))

freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

wheel_1 = Servo(servo_pwm, min_us, max_us, dead_zone_us, freq)
wheel_2 = Servo(servo_pwm2, min_us, max_us, dead_zone_us, freq)

move = MovementSubsystem(wheel_1, wheel_2)

move.move_forward()
print("Moving Forward")
sleep_ms(1000)
move.stop()
sleep_ms(1000)

move.move_backward()
print("Moving Backward")
sleep_ms(1000)
move.stop()
sleep_ms(1000)

move.turn_left()
print("Turning Left")
sleep_ms(500)
move.stop()
sleep_ms(1000)

move.turn_right()
print("Turning Right")
sleep_ms(500)
move.stop()
sleep_ms(1000)