class RobotController:
    def __init__(self, movement, detection):
        self.__movement = movement
        self.__detection = detection
        self.state = "DRIVING"

    def driving_state(self):
        # Set driving state
        self.state = "DRIVING"
        self.__movement.move_forward()

    def update(self):
        # Read sensors
        f_obstacle = self.__detection.sensor_1_obstacle_detected()
        r_obstacle = self.__detection.sensor_2_obstacle_detected()

        # State machine logic
        if self.state == "DRIVING":
            if f_obstacle and r_obstacle:
                # Turn left if there are obstacles front and right
                self.state = "AVOIDING OBSTACLES"
                self.__movement.turn_left()
                print("State:", self.state)
            elif f_obstacle:
                # Turn right if there are only obstacles in front
                self.state = "AVOIDING OBSTACLES"
                self.__movement.turn_right()
                print("State:", self.state)
            else:
                # Move forward if there are no obstacles
                self.__movement.move_forward()
                print("State: DRIVING")
        
        elif self.state == "AVOIDING OBSTACLES":
            # Check if obstacles are cleared
            if f_obstacle and r_obstacle:
                self.__movement.turn_left()
            elif f_obstacle:
                self.__movement.turn_right()
            else:
                self.state = "DRIVING"
                self.__movement.move_forward()
                print("State:", self.state)