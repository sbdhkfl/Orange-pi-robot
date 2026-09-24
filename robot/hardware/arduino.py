import time
try:
    import serial
except ImportError:
    serial = None

class ArduinoRobot:
    def __init__(self, port, baud=115200):
        self.port = port
        self.baud = baud
        self.ser = None

    def connect(self):
        if serial is None:
            raise RuntimeError("Install dependencies with: pip install -r robot/requirements.txt")
        self.ser = serial.Serial(self.port, self.baud, timeout=0.25)
        time.sleep(2)
        self.ser.reset_input_buffer()
        print("Arduino connected:", self.port)

    def send(self, command):
        if self.ser is None:
            raise RuntimeError("Arduino is not connected")
        self.ser.write((command.strip().upper() + "\n").encode("ascii"))
        self.ser.flush()

    def forward(self): self.send("FORWARD")
    def backward(self): self.send("BACKWARD")
    def left(self): self.send("LEFT")
    def right(self): self.send("RIGHT")
    def stop(self):
        if self.ser is not None:
            self.send("STOP")

    def request_status(self):
        self.send("STATUS")
        deadline = time.monotonic() + 1.0
        lines = []
        while time.monotonic() < deadline:
            line = self.ser.readline().decode("utf-8", errors="replace").strip()
            if line:
                lines.append(line)
                if line.startswith("STATUS:"):
                    break
        return "\n".join(lines) if lines else "No status response"

    def close(self):
        if self.ser is not None:
            self.ser.close()
            self.ser = None
