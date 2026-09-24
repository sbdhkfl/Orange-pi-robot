# Orange Pi Robot Wiring

## Orange Pi to Arduino Uno

- Orange Pi TXD0 -> Arduino RX0 (D0)
- Orange Pi RXD0 -> Arduino TX1 (D1)
- Orange Pi GND -> Arduino GND

### Critical voltage warning

The Orange Pi uses 3.3V GPIO while the Uno uses 5V logic. Do not connect a 5V Uno TX signal directly to an Orange Pi RX GPIO. Use a proper level shifter.

The Uno D0/D1 pins are also used for USB serial programming, so disconnect/manage the UART connection while uploading the Arduino sketch.

## MP3/audio module

Planned UART:
- Orange Pi TXD2 -> module RX
- Orange Pi RXD2 -> module TX
- 5V -> module power
- GND -> module GND

Verify the module logic-voltage requirements before making the UART connection.

## Ultrasonic sensor

Connect the sensor to the Arduino. Typical signals are VCC, GND, TRIG and ECHO. Exact Arduino pins must match the firmware.

## USB camera

Connect the USB camera directly to the Orange Pi. Linux should expose a UVC camera as a /dev/video* device.

## Motors

The four motors connect through the L293D motor-driver shield. Do not power motors directly from Orange Pi GPIO.

## Fan

Do not connect a fan directly to Orange Pi GPIO. Use an appropriate transistor/MOSFET or driver circuit and flyback protection where required.
