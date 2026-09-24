# Orange Pi AI Robot

An open-source robotics project built around an Orange Pi Zero 3 and Arduino Uno.

## Main hardware

- Orange Pi Zero 3 (2GB)
- 64GB microSD
- Arduino Uno
- L293D motor-driver shield
- 4 gear motors
- Ultrasonic distance sensor
- USB camera
- Audio module + speaker
- Optional IR cliff sensor
- Fan with a proper driver circuit

## Architecture

**Orange Pi = main computer and intelligence**  
**Arduino Uno = real-time motor/sensor controller**

This is a completely separate project from the ESP32 XiaoZhi Bot.

## Planned capabilities

- 4-wheel movement
- Obstacle avoidance
- USB-camera vision
- Face detection/recognition
- Object detection
- Voice commands when a microphone is available
- Local/open-source assistant features
- Internet knowledge/search
- Audio responses
- Unknown-person photo notifications
- Fan control

## Build order

1. Orange Pi/Linux
2. Wi-Fi
3. USB camera
4. Arduino serial
5. Motors
6. Ultrasonic sensor
7. Audio
8. Vision
9. Recognition
10. Assistant
11. Autonomous behavior
12. Notifications

## Safety

Never connect 5V Arduino UART signals directly to Orange Pi 3.3V GPIO. Use appropriate level shifting. Motors must be powered through the motor driver, not directly from Orange Pi GPIO.

See the docs folder for the detailed project plan and wiring information.

## Security

Never commit Wi-Fi passwords, email passwords, API keys, or other secrets.
