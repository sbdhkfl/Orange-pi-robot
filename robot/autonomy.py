import time

class ObstacleAvoider:
    def __init__(self, robot, sensors, stop_distance=20):
        self.robot = robot
        self.sensors = sensors
        self.stop_distance = stop_distance

    def drive_forward_safely(self):
        if self.sensors.obstacle_ahead(self.stop_distance):
            self.robot.stop()
            return False
        self.robot.forward()
        return True

    def patrol_step(self):
        if self.drive_forward_safely():
            return "FORWARD"
        self.robot.stop()
        time.sleep(0.25)
        self.robot.right()
        time.sleep(0.5)
        self.robot.stop()
        return "AVOIDED"
