# 03 - Complete Hardware List

## Main computer and control

| Hardware | Qty | Job |
|---|---:|---|
| Orange Pi Zero 3 2GB | 1 | Main robot computer |
| 64GB microSD | 1 | Operating system and software |
| Arduino Uno | 1 | Real-time motor/sensor controller |
| L293D motor driver shield | 1 | Drives the four motors |

## Movement

| Hardware | Qty | Job |
|---|---:|---|
| Gear motors | 4 | 4WD movement |
| 4WD chassis | 1 | Holds motors/electronics |
| Wheels | 4 | Robot movement |
| Motor power source | 1 | Powers motors through the motor-driver architecture |

## Sensors

- HC-SR04 or compatible ultrasonic distance sensor
- IR cliff/edge sensor, if retained in the build
- USB camera connected directly to Orange Pi Zero 3

## Audio

- MP3/audio module
- speaker
- suitable amplifier if required by the selected speaker/module
- audio storage/module media as required by the chosen MP3 module

## Other

- cooling fan
- jumper wires
- USB cable for Arduino
- stable Orange Pi power supply
- suitable motor battery/power source
- common-ground wiring
- chassis mounting hardware

## Explicit project exclusions

- OLED display: removed
- ESP32-CAM: removed from the vision path
- Orange Pi -> home ESP device control: excluded
- paid/proprietary AI APIs: excluded

The USB camera is connected directly to the Orange Pi.
