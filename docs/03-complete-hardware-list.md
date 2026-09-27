# 03 - Complete Hardware List

Here is the full hardware list for the robot.

## Brain and controller
| Hardware | Qty | Job |
|---|---:|---|
| Orange Pi Zero 3 2GB | 1 | Main computer and AI |
| 64GB microSD card | 1 | OS and robot software |
| Arduino Uno | 1 | Motor and sensor controller |
| L293D motor-driver shield | 1 | Drives the four motors |

## Movement
| Hardware | Qty | Job |
|---|---:|---|
| Gear motors | 4 | Moves the robot |
| 4WD chassis | 1 | Holds everything |
| Wheels | 4 | Lets the robot move |
| Motor power source | 1 | Powers the motors through the driver |

## Sensors and vision
- HC-SR04 or compatible ultrasonic distance sensor
- USB camera connected directly to the Orange Pi

## Audio
- MP3/audio module
- Speaker
- Audio storage/media required by the selected audio module
- Amplifier if the selected speaker/module needs one

## Cooling and build supplies
- Fan
- Jumper wires
- USB cable for the Arduino
- Stable Orange Pi power supply
- Motor battery/power source
- Mounting hardware
- Chassis hardware
- Common-ground wiring where needed

## The basic idea
The Orange Pi does the thinking.

The Arduino does the fast motor and sensor work.

The L293D shield sits on the Arduino and drives the four motors.

The USB camera plugs directly into the Orange Pi.

The audio module handles the robot audio output.