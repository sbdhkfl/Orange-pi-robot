# 04 - Complete Wiring

This is the wiring plan we are using for the robot.

## 1. Orange Pi <-> Arduino Uno
| Orange Pi | Arduino Uno |
|---|---|
| TXD0 | RX0 / digital pin 0 |
| RXD0 | TX1 / digital pin 1 |
| GND | GND |

Important: the voltage levels have to be safe for both boards. The Orange Pi GPIO side is 3.3V, so we use proper level shifting or another safe UART setup when needed.

The Orange Pi sends high-level commands.

The Arduino handles the fast motor and sensor work.

## 2. Arduino + L293D shield + four motors
Put the L293D shield on the Arduino Uno.

Then connect the four motors to the four motor outputs on the shield.

- Motor 1 -> Motor output A
- Motor 2 -> Motor output B
- Motor 3 -> Motor output C
- Motor 4 -> Motor output D

Use the labels printed on your exact shield for the final terminal names.

If one motor spins the wrong way, swap that motor two wires.

The motors get power from the motor power input. They do not get powered from an Orange Pi GPIO.

## 3. Ultrasonic sensor
For a typical HC-SR04:

| HC-SR04 | Arduino |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | Arduino digital output used by the firmware |
| ECHO | Arduino digital input used by the firmware |

The exact digital pins are whatever we define in the Arduino code. The wiring and code have to match.

## 4. USB camera
**USB camera -> Orange Pi USB port**

The camera talks directly to the Orange Pi.

Linux/OpenCV handles the camera.

## 5. MP3/audio module
The planned UART connection is:

| Orange Pi | Audio module |
|---|---|
| TXD2 | RX |
| RXD2 | TX |
| 5V | VCC, only when the module requires 5V |
| GND | GND |

TX and RX cross over.

If the audio module needs an amplifier for the speaker, the audio path is:

**Audio module -> amplifier -> speaker**

## 6. Fan
The fan should be controlled through a proper transistor/MOSFET driver circuit.

Do not connect a fan directly to an Orange Pi GPIO.

The GPIO controls the driver, and the driver controls the fan power.

## 7. Power
Keep the power setup simple:
- Orange Pi gets its own stable power
- Arduino/control electronics get the correct power
- Motors get the motor power they need
- Audio hardware gets its required power
- Grounds are connected where the signal design requires a common reference

Try to keep high-current motor wires away from sensitive signal wires.

## 8. The wiring order
Do not wire everything and then try to debug it all at once.

Do it like this:
1. Orange Pi power
2. Arduino power
3. UART
4. L293D shield
5. One motor
6. All four motors
7. Ultrasonic sensor
8. USB camera
9. Audio
10. Fan

After every step, test it before moving on.