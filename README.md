# Orange Pi AI Robot 🤖

This is the big robot project built around the Orange Pi Zero 3 and Arduino Uno.

The simple way to think about it is:

**Orange Pi = the brain**

**Arduino Uno = the part that handles the motors and sensors**

That way each board has a job and it is way easier to test everything.

## Main hardware
- Orange Pi Zero 3 2GB
- 64GB microSD card
- Arduino Uno
- L293D motor-driver shield
- 4 gear motors
- 4WD chassis and wheels
- Ultrasonic distance sensor
- USB camera
- MP3/audio module
- Speaker
- Fan
- Motor power source
- Stable Orange Pi power supply
- USB cable
- Jumper wires and mounting hardware

## What the robot is supposed to do
- Move forward
- Move backward
- Turn left
- Turn right
- Stop
- Avoid obstacles
- See things with the USB camera
- Recognize known people
- Greet known people
- Take a picture when an unknown person is detected
- Send an alert when configured
- Detect objects
- Learn/register objects
- Understand commands about detected objects
- Use local/open-source AI features
- Search the Internet when Internet is available
- Talk back with audio
- Control the fan
- Run autonomous behaviors when we enable them

## How it works
The Orange Pi handles the big stuff like vision, AI, networking, audio, storage, and the main robot program.

The Arduino handles the stuff that needs to happen quickly, like motors and sensors.

## Build order
1. Set up Orange Pi
2. Set up Wi-Fi
3. Test the USB camera
4. Test Orange Pi to Arduino communication
5. Test the motor driver
6. Test all four motors
7. Test the ultrasonic sensor
8. Test audio
9. Add vision
10. Add face recognition
11. Add object detection
12. Add the assistant
13. Add autonomous behavior
14. Add alerts

We will test each step before stacking the next one on top.

## Important wiring rule
The Orange Pi uses 3.3V GPIO.

The Arduino side can use 5V logic.

So the UART connection has to use compatible voltage levels. We do not just connect an unsafe voltage straight into an Orange Pi GPIO.

Also, the motors get their power through the motor driver, not from an Orange Pi GPIO.

## Security
Do not put Wi-Fi passwords, email passwords, API keys, or other private information into the GitHub repo.