class RobotController:
    def __init__(self, movement, detection):
        self.__movement = movement
        self.__detection = detection
        self.state = "IDLE"
    
    def idle_state(self):
        # Set idle state
        self.state = "IDLE"
        self.__movement.stop()

    def driving_state(self):
        # Set driving state
        self.state = "DRIVING"
        self.__movement.move_forward()
    
    def reversing_state(self):
        # Set reversing state
        self.state = "REVERSING"
        self.__movement.move_backward()
    
    def turning_left_state(self):
        # Set left turning state
        self.state = "TURNING LEFT"
        self.__movement.turn_left()
    
    def turning_right_state(self):
        # Set right turning state
        self.state = "TURNING RIGHT"
        self.__movement.turn_right()

    def avoid_state_1(self):
        # Set avoiding state 1
        self.state = "AVOIDING OBSTACLES"
        self.__movement.stop()
        self.__movement.turn_right()
    
    def avoid_state_2(self):
        # Set avoiding state 2
        self.state = "AVOIDING OBSTACLES"
        self.__movement.stop()
        self.__movement.turn_left()
    
    def update(self):
        # Read sensors
        f_obstacle = self.__detection.sensor_1_obstacle_detected()
        r_obstacle = self.__detection.sensor_2_obstacle_detected()

        # State machine logic
        if self.state == "IDLE":
            self.__movement.stop()

        elif self.state == "DRIVING":
            self.__movement.move_forward()
            if f_obstacle and r_obstacle:
                self.avoid_state_2()
            elif f_obstacle:
                self.avoid_state_1()
        
        elif self.state == "AVOIDING OBSTACLES":
            # Check if obstacles are cleared
            if not f_obstacle:
                self.driving_state()
        
        elif self.state == "REVERSING":
            self.__movement.move_backward()