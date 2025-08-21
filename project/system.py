from servo import Servo
from machine import Pin, PWM
from PiicoDev_Unified import sleep_ms
from controller import RobotController
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from subsystems import MovementSubsystem, DetectionSubsystem

class RobotSystem:
    def __init__(self, wheel_1, wheel_2, f_sensor, r_sensor, threshold_1=100, threshold_2=40):
        # Set up movement
        self.movement = MovementSubsystem(wheel_1, wheel_2)
        # Set up detection
        self.detection = DetectionSubsystem(f_sensor, r_sensor, threshold_1, threshold_2)
        # Set up controller
        self.controller = RobotController(self.movement, self.detection)
    
    def run(self):
        while True:
            self.controller.update()
            sleep_ms(100)

# Define the wheels
wheel_1 = Servo(PWM(Pin(16)), 500, 2500, 1500, 500)
wheel_2 = Servo(PWM(Pin(20)), 500, 2500, 1500, 500)

#Define the sensors
f_sensor = PiicoDev_Ultrasonic(id=[0,0,0,0])
r_sensor = PiicoDev_Ultrasonic(id=[0,0,1,0])

# Create the robot system
robot = RobotSystem(wheel_1, wheel_2, f_sensor, r_sensor)

# Start robot running
robot.run()