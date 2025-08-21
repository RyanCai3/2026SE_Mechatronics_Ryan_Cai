class RobotController:
    def __init__(self, movement, detection):
        self.__movement = movement
        self.__detection = detection
        self.state = "DRIVING"

    def driving_state(self):
        self.state = "DRIVING"
        self.__movement.move_forward()

    def turning_left_state(self):
        self.state = "TURNING LEFT"
        self.__movement.turn_left()

    def turning_right_state(self):
        self.state = "TURNING RIGHT"
        self.__movement.turn_right()

    def avoid_state_1(self):
        # Turn right to avoid obstacle
        self.state = "AVOIDING OBSTACLES"
        self.__movement.stop()
        self.__movement.turn_right()

    def avoid_state_2(self):
        # Turn left if both sensors detect obstacles
        self.state = "AVOIDING OBSTACLES"
        self.__movement.stop()
        self.__movement.turn_left()

    def update(self):
        f_obstacle = self.__detection.sensor_1_obstacle_detected()
        r_obstacle = self.__detection.sensor_2_obstacle_detected()

        if self.state == "IDLE":
            self.__movement.stop()
            print("State:", self.state)

        elif self.state == "DRIVING":
            self.__movement.move_forward()
            
            if f_obstacle and r_obstacle:
                self.avoid_state_2()
                print("State:", self.state)
            
            elif f_obstacle:
                self.avoid_state_1()
                print("State:", self.state)

        elif self.state == "AVOIDING OBSTACLES":
            # Check if front obstacle cleared
            if not f_obstacle:
                self.driving_state()
                print("State:", self.state)

        elif self.state == "REVERSING":
            self.__movement.move_backward()
            print("State:", self.state)