class MovementSubsystem:
    def __init__(self, wheel_1, wheel_2):
        self.__wheel_1 = wheel_1 # First wheel
        self.__wheel_2 = wheel_2 # Second wheel

    def stop(self):
        # Stops the robot
        self.__wheel_1.set_duty(1500)
        self.__wheel_2.set_duty(1500)

    def move_forward(self):
        # Moves forward
        self.__wheel_1.set_duty(2000)
        self.__wheel_2.set_duty(1000)

    def move_backward(self):
        # Moves backward
        self.__wheel_1.set_duty(1000)
        self.__wheel_2.set_duty(2000)

    def turn_left(self):
        # Turns left
        self.__wheel_1.set_duty(1400)
        self.__wheel_2.set_duty(1400)
    
    def turn_right(self):
        # Turns right
        self.__wheel_1.set_duty(1600)
        self.__wheel_2.set_duty(1600)

class DetectionSubsystem:
    def __init__(self, sensor_1, sensor_2, threshold_1_mm, threshold_2_mm):
        self.__sensor_1 = sensor_1 # First sensor
        self.__sensor_2 = sensor_2 # Second sensor
        self.__threshold_1 = threshold_1_mm # Obstacle threshold for sensor 1
        self.__threshold_2 = threshold_2_mm # Obstacle threshold for sensor 2
    
    def get_distance_sensor_1(self):
        # Return distance (mm) for sensor 1
        return self.__sensor_1.distance_mm()
    
    def get_distance_sensor_2(self):
        # Return distance (mm) for sensor 2
        return self.__sensor_2.distance_mm()

    def sensor_1_obstacle_detected(self):
        # Check if a sensor 1 detects an obstacle
        return self.get_distance_sensor_1() < self.__threshold_1
    
    def sensor_2_obstacle_detected(self):
        # Check if a sensor 2 detects an obstacle
        return self.get_distance_sensor_2() < self.__threshold_2
    
    def any_obstacle(self):
        # Return "true" if either sensor detects an obstacle
        return self.sensor_1_obstacle_detected() or self.sensor_2_obstacle_detected()