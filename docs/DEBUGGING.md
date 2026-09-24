# Debugging guide

This guide is for common failures in the project.

## Orange Pi robot

### No serial connection
- Confirm the Arduino sketch is uploaded.
- Confirm the UART device with: ls /dev/ttyS*
- Confirm the configured port in .env.
- Make sure TX and RX are crossed and grounds are shared.
- Do not connect 5 V logic directly into an Orange Pi GPIO input.

### Motors do not move
- Test with wheels lifted off the ground.
- Verify the L293D shield pin mapping against the exact board.
- Verify motor power and common ground.
- Test each motor output separately.
- Check that D0/D1 are not still connected while uploading to the Uno.

### Robot moves the wrong direction
- Swap the two motor wires for the affected motor, or invert that motor in the controller.
- Check left/right motor grouping.

### Ultrasonic readings are -1 or unreasonable
- Check VCC, GND, TRIG and ECHO.
- Check the sensor's voltage compatibility.
- Verify the configured pins.
- Keep the sensor away from loose wires and vibrating mounts.

### USB camera is not found
- Run: ls /dev/video*
- Run: v4l2-ctl --list-devices if v4l-utils is installed.
- Try the correct video device number in ROBOT_CAMERA.
- Check the USB cable and power.
- Test a low resolution such as 640x480.

### Camera opens but captures black frames
- Check the selected /dev/video device.
- Test another supported pixel format or resolution with v4l2-ctl.
- Make sure another program is not using the camera.

### Python import errors
- Use a virtual environment.
- Run: pip install -r robot/requirements.txt
- Confirm the same Python interpreter is running the program.

### Email does not send
- Keep credentials in .env, never in Git.
- For Gmail, use an account/app-password setup appropriate for the account instead of putting a normal account password in source code.
- Confirm SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD and ALERT_TO.
- Test network access from the Orange Pi.

### Face detection does not start
- A compatible local model file is required.
- Put the model path in the application configuration.
- Recognition is separate from detection and requires an enrollment/recognition system.

### Object detection returns nothing
- The repository provides an adapter, not a bundled trained model.
- Install a compatible local model and connect it to ObjectDetector.
- Confirm the model is small enough for the Orange Pi's available CPU/RAM.

## ESP32 XiaoZhi Bot

### ESP32 is not detected
- Try another USB data cable.
- Try another USB port.
- Install the correct USB-to-serial driver for the board.
- Hold BOOT while starting an upload if the board requires manual download mode.

### Upload fails
- Select the correct board and port.
- Close serial monitors using the port.
- Lower upload speed if the board or cable is unreliable.
- Reset the board and retry.

### Wi-Fi does not connect
- Verify SSID and password.
- Check that the network is available to the board.
- Print connection status and retry with a timeout.
- Do not hard-code credentials in public source files.

### Audio input is not working
- Verify microphone wiring and power.
- Check the exact microphone hardware used by the XiaoZhi firmware.
- Confirm the selected audio input pins/configuration.
- Test the microphone separately before debugging AI features.

### Speaker/audio output is not working
- Check amplifier power and ground.
- Verify I2S pins and configuration.
- Make sure the speaker is connected through the appropriate amplifier when required.
- Test a known-good audio sample.

### Device resets repeatedly
- Check power stability.
- Disconnect motors or other high-current peripherals during testing.
- Inspect serial logs for brownout or watchdog messages.
- Reduce peripheral load and test the board alone.

### MCP/network endpoint does not respond
- Confirm the endpoint is reachable from the same network.
- Check the server logs.
- Confirm the URL and port in the ESP32 configuration.
- Add timeouts and error handling so a network failure cannot lock the device.

### General rule
Change one thing at a time, record the exact error message, and test the smallest possible component before combining features.
