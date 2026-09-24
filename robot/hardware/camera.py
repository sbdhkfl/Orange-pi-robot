from datetime import datetime
from pathlib import Path

class Camera:
    def __init__(self, device=2, output_dir="captures"):
        self.device = device
        self.output_dir = Path(output_dir)
        self.cap = None

    def _open(self):
        try:
            import cv2
        except ImportError as exc:
            raise RuntimeError("Install OpenCV with robot/requirements.txt") from exc
        if self.cap is None:
            self.cap = cv2.VideoCapture(self.device, cv2.CAP_V4L2)
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open /dev/video" + str(self.device))
        return cv2

    def capture(self):
        cv2 = self._open()
        ok, frame = self.cap.read()
        if not ok:
            raise RuntimeError("Camera opened but no frame was received.")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        filename = self.output_dir / datetime.now().strftime("capture_%Y%m%d_%H%M%S.jpg")
        if not cv2.imwrite(str(filename), frame):
            raise RuntimeError("Could not save camera frame.")
        return str(filename)

    def close(self):
        if self.cap is not None:
            self.cap.release()
            self.cap = None
