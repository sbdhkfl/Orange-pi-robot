# Robot software

This directory contains the Orange Pi side of the robot.

## Quick start

1. Install Python 3 and a camera/serial environment.
2. Create a virtual environment:
   python3 -m venv .venv
   source .venv/bin/activate
3. Install dependencies:
   pip install -r robot/requirements.txt
4. Copy config.example.env to .env and edit it.
5. Upload robot/arduino/robot_controller.ino to the Uno.
6. Reconnect UART only after uploading.
7. Run:
   python3 robot/main.py

The current main program supports manual drive, status, and camera capture.

## Modules already included

- hardware/arduino.py: Orange Pi to Uno serial control
- hardware/camera.py: USB camera capture
- hardware/sensors.py: ultrasonic status helpers
- autonomy.py: simple obstacle-aware forward/patrol logic
- assistant/commands.py: local text command parsing
- notifications/email.py: optional SMTP email with JPEG attachment
- vision/detection.py: optional local OpenCV face detection adapter
- vision/objects.py: local object detector adapter
- vision/face_registry.py: simple enrollment registry

## Important

Face recognition and object detection are model-dependent. The repository includes the software interfaces, but does not pretend those features are fully trained or tested until a compatible local model is installed and tested on the Orange Pi.

Never commit passwords, SMTP app passwords, private keys, or personal photos.
