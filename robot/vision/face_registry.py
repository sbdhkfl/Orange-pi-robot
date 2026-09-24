import json
from pathlib import Path

class FaceRegistry:
    def __init__(self, path="data/faces.json"):
        self.path = Path(path)

    def load(self):
        if not self.path.exists():
            return {}
        return json.loads(self.path.read_text())

    def save(self, people):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(people, indent=2))

    def add(self, name, image_path):
        people = self.load()
        people[name] = {"image": str(image_path)}
        self.save(people)
