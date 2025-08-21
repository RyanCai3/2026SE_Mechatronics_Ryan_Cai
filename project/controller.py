from PiicoDev_Unified import sleep_ms

class RobotController:
    def __init__(self, movement, detection):
        self.__movement = movement
        self.__detection = detection
        self.state = "DRIVING"

    def driving_state(self):
        # Set driving state
        self.state = "DRIVING"
        self.__movement.move_forward()

    def avoid_state_1(self):
        # Set avoiding state 1
        self.__movement.stop()
        sleep_ms(500)
        self.state = "AVOIDING OBSTACLES"
        self.__movement.turn_left()

    def avoid_state_2(self):
        # Set avoiding state 2
        self.__movement.stop()
        sleep_ms(500)
        self.state = "AVOIDING OBSTACLES"
        self.__movement.turn_right()

    def update(self):
        # Read sensors
        f_obstacle = self.__detection.sensor_1_obstacle_detected()
        r_obstacle = self.__detection.sensor_2_obstacle_detected()

        # State machine logic
        if self.state == "DRIVING":
            self.__movement.move_forward()
            if f_obstacle and r_obstacle:
                self.avoid_state_1()
                sleep_ms(500)
            elif f_obstacle:
                self.avoid_state_2()
                sleep_ms(500)
            else:
                self.driving_state()

        elif self.state == "AVOIDING OBSTACLES":
            # Check if obstacles are cleared
            if not f_obstacle:
                self.driving_state()