# Arduino Controller

Open robot_controller.ino in Arduino IDE.

Before uploading:
1. Disconnect the Orange Pi UART wires from Arduino D0/D1.
2. Upload the sketch over USB.
3. Reconnect the UART after uploading.
4. Test with the wheels lifted off the ground.

The Arduino Uno R3 uses D0 and D1 for the board's digital I/O/serial interface. The exact L293D shield pinout varies by shield, so verify the pins printed by your board before driving motors.
