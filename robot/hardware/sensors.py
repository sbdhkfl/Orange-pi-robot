import time

class SensorSuite:
    def __init__(self, arduino):
        self.arduino = arduino

    def status(self):
        return self.arduino.request_status()

    def distance_cm(self):
        status = self.status()
        marker = "DISTANCE="
        if marker not in status:
            return None
        try:
            value = status.split(marker, 1)[1].split()[0]
            return float(value)
        except (ValueError, IndexError):
            return None

    def obstacle_ahead(self, threshold_cm=20):
        distance = self.distance_cm()
        return distance is not None and distance >= 0 and distance < threshold_cm

    def wait_until_clear(self, threshold_cm=20, timeout=10):
        end = time.monotonic() + timeout
        while time.monotonic() < end:
            if not self.obstacle_ahead(threshold_cm):
                return True
            time.sleep(0.25)
        return False
