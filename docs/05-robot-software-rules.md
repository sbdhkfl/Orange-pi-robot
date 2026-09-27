# 05 - Project Rules and Feature Set

## Required capabilities

- forward/back/left/right/stop
- ultrasonic obstacle avoidance
- USB-camera vision
- face detection and known-person recognition
- greeting known people
- unknown-person photo/email alert when configured
- object detection
- object registration/teaching
- local knowledge
- Internet search when Internet is available
- commands directed toward detected objects
- spoken responses
- fan control
- autonomous/patrol behaviors where configured
- Arduino handles time-sensitive motor and sensor control

## Architecture rule

Orange Pi = high-level intelligence, vision, audio, networking, storage.

Arduino Uno = real-time motor and sensor controller.

This separation makes the robot easier to debug: if motors/sensors fail, test the Arduino side independently; if vision/AI fails, test the Orange Pi side independently.

## Explicit exclusions

- no OLED
- no ESP32-CAM for vision
- no controlling other ESP devices around the home
- no required paid AI API
