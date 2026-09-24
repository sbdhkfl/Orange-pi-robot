/*
  Orange Pi AI Robot Arduino controller.

  Commands from Orange Pi:
  FORWARD
  BACKWARD
  LEFT
  RIGHT
  STOP
  STATUS

  IMPORTANT:
  L293D shields are not all wired the same. These are configurable
  example pins for a common four-channel arrangement. Verify your
  exact shield before connecting motors.

  D0/D1 are reserved for the serial connection.
*/

const unsigned long BAUD_RATE = 115200;

const int M1_A = 3;
const int M1_B = 4;
const int M2_A = 5;
const int M2_B = 6;
const int M3_A = 7;
const int M3_B = 8;
const int M4_A = 11;
const int M4_B = 12;

const int TRIG_PIN = 9;
const int ECHO_PIN = 10;
const long OBSTACLE_CM = 20;

void setupMotorPins() {
  const int pins[] = {M1_A,M1_B,M2_A,M2_B,M3_A,M3_B,M4_A,M4_B};
  for (unsigned int i=0; i<sizeof(pins)/sizeof(pins[0]); i++) {
    pinMode(pins[i], OUTPUT);
    digitalWrite(pins[i], LOW);
  }
}

void setup() {
  Serial.begin(BAUD_RATE);
  setupMotorPins();
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  digitalWrite(TRIG_PIN, LOW);
  stopMotors();
  Serial.println("READY");
}

void setMotor(int a, int b, int direction) {
  if (direction > 0) {
    digitalWrite(a, HIGH);
    digitalWrite(b, LOW);
  } else if (direction < 0) {
    digitalWrite(a, LOW);
    digitalWrite(b, HIGH);
  } else {
    digitalWrite(a, LOW);
    digitalWrite(b, LOW);
  }
}

void setLeftSide(int direction) {
  setMotor(M1_A, M1_B, direction);
  setMotor(M3_A, M3_B, direction);
}

void setRightSide(int direction) {
  setMotor(M2_A, M2_B, direction);
  setMotor(M4_A, M4_B, direction);
}

void stopMotors() {
  setLeftSide(0);
  setRightSide(0);
}

void moveForward() {
  setLeftSide(1);
  setRightSide(1);
}

void moveBackward() {
  setLeftSide(-1);
  setRightSide(-1);
}

void turnLeft() {
  setLeftSide(-1);
  setRightSide(1);
}

void turnRight() {
  setLeftSide(1);
  setRightSide(-1);
}

long readDistanceCm() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(3);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  unsigned long duration = pulseIn(ECHO_PIN, HIGH, 25000UL);
  if (duration == 0) return -1;
  return (long)(duration / 58UL);
}

void handleCommand(String command) {
  command.trim();
  command.toUpperCase();

  if (command == "FORWARD") {
    long distance = readDistanceCm();
    if (distance > 0 && distance < OBSTACLE_CM) {
      stopMotors();
      Serial.println("BLOCKED");
      return;
    }
    moveForward();
    Serial.println("OK:FORWARD");
  } else if (command == "BACKWARD") {
    moveBackward();
    Serial.println("OK:BACKWARD");
  } else if (command == "LEFT") {
    turnLeft();
    Serial.println("OK:LEFT");
  } else if (command == "RIGHT") {
    turnRight();
    Serial.println("OK:RIGHT");
  } else if (command == "STOP") {
    stopMotors();
    Serial.println("OK:STOP");
  } else if (command == "STATUS") {
    Serial.print("STATUS:DISTANCE=");
    Serial.println(readDistanceCm());
  } else {
    Serial.print("ERROR:UNKNOWN_COMMAND=");
    Serial.println(command);
  }
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    handleCommand(command);
  }
}
