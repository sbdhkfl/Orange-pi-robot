class ObjectDetector:
    """Adapter for a local object-detection model.

    The robot intentionally does not download a proprietary model or call a
    paid cloud API. Plug in a compatible local model later.
    """

    def __init__(self, model=None):
        self.model = model

    def detect(self, frame):
        if self.model is None:
            return []
        return self.model(frame)
