# 05 - Robot Software Rules

This is what the robot software is supposed to cover.

## Movement
- Forward
- Backward
- Left
- Right
- Stop
- 4WD motor control

## Sensors
- Ultrasonic obstacle detection
- Safe motor stopping when an obstacle is too close

## Vision
- USB camera input
- Face detection
- Known-person recognition
- Known-person greetings
- Unknown-person picture capture
- Object detection
- Object registration/teaching

## Assistant
- Voice commands when the audio input hardware is available
- Local/open-source AI features
- Local knowledge
- Internet search when Internet is available
- Commands about objects the camera can see
- Audio responses

## Robot extras
- Fan control
- Autonomous movement
- Patrol behavior
- Configurable alerts

## How we split the work
**Orange Pi:** vision, AI, networking, storage, audio, and the main robot program.

**Arduino Uno:** motors, ultrasonic sensor, and other real-time control.

This makes debugging way easier because we can test the Orange Pi side and Arduino side separately.

## Project rules
- Keep the important software open-source friendly
- Do not require paid AI APIs
- Do not put passwords or API keys in the repo
- Make every hardware connection clear
- Make every setup step copy-paste friendly
- Test every feature before calling it finished