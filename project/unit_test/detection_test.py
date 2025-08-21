from PiicoDev_Unified import sleep_ms
from controller import DetectionSubsystem
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic

f_sensor = PiicoDev_Ultrasonic(id=[0,0,0,0])
r_sensor = PiicoDev_Ultrasonic(id=[0,0,1,0])

threshold_1_mm = 100
threshold_2_mm = 40

detection = DetectionSubsystem(f_sensor, r_sensor, threshold_1_mm, threshold_2_mm)

while True:
    print(f"Front Sensor: {detection.get_distance_sensor_1()} mm")
    print(f"Right Sensor: {detection.get_distance_sensor_2()} mm")
    sleep_ms(1000)

    if detection.sensor_1_obstacle_detected():
        print("Obstacle Detected In Front!")

    if detection.sensor_2_obstacle_detected():
        print("Obstacle Detected On Right!")

    if not detection.any_obstacle():
        print("Path Clear!")