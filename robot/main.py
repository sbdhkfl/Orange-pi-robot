#!/usr/bin/env python3
import os
from dotenv import load_dotenv

from hardware.arduino import ArduinoRobot
from hardware.camera import Camera
from hardware.sensors import SensorSuite
from assistant.commands import execute
from autonomy import ObstacleAvoider
from notifications.email import EmailNotifier

load_dotenv()

SERIAL_PORT = os.getenv("ROBOT_SERIAL_PORT", "/dev/ttyS0")
BAUD_RATE = int(os.getenv("ROBOT_BAUD", "115200"))
CAMERA_DEVICE = int(os.getenv("ROBOT_CAMERA", "2"))

def main():
    robot = ArduinoRobot(SERIAL_PORT, BAUD_RATE)
    camera = Camera(CAMERA_DEVICE, os.getenv("CAPTURE_DIR", "captures"))
    sensors = SensorSuite(robot)
    autonomy = ObstacleAvoider(robot, sensors)
    email = EmailNotifier()

    print("Orange Pi AI Robot")
    print("Commands: forward, backward, left, right, stop, status, photo, patrol, email-test, quit")

    try:
        robot.connect()
        while True:
            text = input("> ").strip()
            command = text.lower()

            if command in ("quit", "q", "exit"):
                break

            if command in ("patrol", "auto"):
                result = autonomy.patrol_step()
                print(result)
                continue

            if command in ("email-test", "test email"):
                ok, message = email.send("Orange Pi Robot test", "The robot email system is working.")
                print(message)
                continue

            result = execute(robot, camera, text)
            print(result)

    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        robot.stop()
        robot.close()
        camera.close()

if __name__ == "__main__":
    main()
