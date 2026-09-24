#!/usr/bin/env python3
import os
from hardware.arduino import ArduinoRobot
from hardware.camera import Camera

SERIAL_PORT = os.getenv("ROBOT_SERIAL_PORT", "/dev/ttyS0")
BAUD_RATE = int(os.getenv("ROBOT_BAUD", "115200"))
CAMERA_DEVICE = int(os.getenv("ROBOT_CAMERA", "2"))

def main():
    robot = ArduinoRobot(SERIAL_PORT, BAUD_RATE)
    camera = Camera(CAMERA_DEVICE)
    print("Orange Pi Robot")
    print("w=forward s=backward a=left d=right x=stop c=capture status=q=quit")
    try:
        robot.connect()
        while True:
            command = input("> ").strip().lower()
            if command in ("w", "forward"): robot.forward()
            elif command in ("s", "backward"): robot.backward()
            elif command in ("a", "left"): robot.left()
            elif command in ("d", "right"): robot.right()
            elif command in ("x", "stop"): robot.stop()
            elif command == "status": print(robot.request_status())
            elif command == "c": print("Saved:", camera.capture())
            elif command == "q": break
            elif command in ("help", "?"): print("w/s/a/d/x/c/status/q")
            elif command: print("Unknown command")
    except KeyboardInterrupt:
        print("\nStopping...")
    finally:
        robot.stop()
        robot.close()
        camera.close()

if __name__ == "__main__":
    main()
