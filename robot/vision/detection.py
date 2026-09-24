from pathlib import Path

class FaceDetector:
    """Optional local face detector using OpenCV's bundled DNN APIs.

    This module only detects faces. Recognition requires enrolled reference
    data and a recognition model; it is intentionally kept separate.
    """

    def __init__(self, model_path=None):
        self.model_path = model_path
        self.net = None

    def load(self):
        if not self.model_path or not Path(self.model_path).exists():
            raise RuntimeError("Provide a local face detection model file.")
        import cv2
        self.net = cv2.FaceDetectorYN.create(
            self.model_path, "", (320, 320), 0.9, 0.3, 5000
        )

    def detect(self, frame):
        if self.net is None:
            self.load()
        import cv2
        h, w = frame.shape[:2]
        self.net.setInputSize((w, h))
        _, faces = self.net.detect(frame)
        return [] if faces is None else faces.tolist()
