# 04 - Complete Wiring

## 1. Arduino Uno <-> Orange Pi

The intended serial link is:

| Orange Pi | Arduino Uno |
|---|---|
| TXD0 | RX0 / digital pin 0 |
| RXD0 | TX1 / digital pin 1 |
| GND | GND |

**Important:** both devices must use compatible logic levels and a safe UART arrangement. Do not connect an incompatible voltage directly to a GPIO.

The Arduino remains responsible for time-sensitive motor/sensor control. The Orange Pi sends high-level commands.

## 2. Arduino + L293D motor shield + four motors

The L293D shield is mounted on the Uno.

- Motor 1 -> shield motor output A
- Motor 2 -> shield motor output B
- Motor 3 -> shield motor output C
- Motor 4 -> shield motor output D

Use the motor shield's documented terminal labels for the exact output names. Motor polarity determines which direction each motor spins; if a motor runs backwards, swap that motor's two wires.

**Do not power the four motors from the Orange Pi's 5V rail.** Use the motor-power input intended by the shield/chassis design and keep the control electronics at their required voltage.

## 3. Ultrasonic sensor

Typical HC-SR04 wiring:

| Sensor | Controller |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | Arduino digital output selected by firmware |
| ECHO | Arduino digital input selected by firmware |

The exact digital pins are defined by the current Arduino firmware and must match its constants.

## 4. IR cliff sensor

| Sensor | Arduino |
|---|---|
| VCC | 5V or the sensor's rated voltage |
| GND | GND |
| OUT | Arduino digital input selected by firmware |

If the sensor is removed from the final build, its code and wiring are disabled rather than left ambiguous.

## 5. USB camera

USB camera -> Orange Pi USB port.

The camera is **not** connected to the Arduino.

The Orange Pi uses Linux V4L2/OpenCV to read the camera.

## 6. MP3/audio module

The intended Orange Pi UART/audio connection is:

| Orange Pi | Audio module |
|---|---|
| TXD2 | RX |
| RXD2 | TX |
| 5V | VCC, only if the module requires 5V |
| GND | GND |

UART TX/RX are crossed.

The audio module drives the speaker according to its electrical requirements. If an amplifier is used, wire the module's audio output to the amplifier input and the amplifier output to the speaker.

## 7. Fan

The fan must not be driven directly from an Orange Pi GPIO. The final circuit should use a suitable transistor/MOSFET driver and flyback protection when required by the fan type.

The Orange Pi/Arduino controls the driver; the fan gets power from its appropriate supply.

## 8. Ground

Where the design requires signals between subsystems, establish the required common ground. Keep high-current motor wiring physically separated from sensitive signal wiring where practical.

## 9. Power architecture

Use separate appropriate power paths for:
- Orange Pi
- Arduino/control electronics
- motors
- audio hardware

Tie grounds together only where required for signal reference.

## 10. Removed hardware

There is no OLED wiring in this project and no ESP32-CAM vision wiring.
