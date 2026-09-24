# Orange Pi Robot Software Architecture

Proposed layout:

robot/
  main.py
  config/
  hardware/arduino.py
  hardware/audio.py
  hardware/camera.py
  hardware/sensors.py
  vision/faces.py
  vision/objects.py
  assistant/commands.py
  assistant/knowledge.py
  assistant/internet.py
  notifications/email.py

## Arduino protocol

Basic movement commands:

FORWARD
BACKWARD
LEFT
RIGHT
STOP

Possible sensor messages:

DISTANCE:35
CLIFF:0

The protocol should stay simple and reliable so the Arduino can keep controlling the motors even if higher-level software temporarily fails.

## Vision pipeline

USB camera -> frame capture -> detection/recognition -> robot action or response.

## Voice pipeline

Microphone -> speech recognition -> command parser -> robot action -> audio response.

A microphone is currently optional.

## Security

Passwords, Wi-Fi credentials, email credentials, and API keys must stay outside Git.
