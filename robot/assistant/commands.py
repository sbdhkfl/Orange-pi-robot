import re

DIRECTION_WORDS = {
    "forward": "FORWARD",
    "ahead": "FORWARD",
    "back": "BACKWARD",
    "backward": "BACKWARD",
    "left": "LEFT",
    "right": "RIGHT",
    "stop": "STOP",
    "halt": "STOP",
}

def parse_command(text):
    text = re.sub(r"[^a-zA-Z0-9 ]+", " ", text.lower()).strip()
    if not text:
        return None

    for word, command in DIRECTION_WORDS.items():
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            return command

    if "status" in text:
        return "STATUS"
    if "camera" in text or "photo" in text or "picture" in text:
        return "CAPTURE"
    if "help" in text:
        return "HELP"
    return None

def execute(robot, camera, text):
    command = parse_command(text)
    if command == "FORWARD":
        robot.forward()
    elif command == "BACKWARD":
        robot.backward()
    elif command == "LEFT":
        robot.left()
    elif command == "RIGHT":
        robot.right()
    elif command == "STOP":
        robot.stop()
    elif command == "STATUS":
        return robot.request_status()
    elif command == "CAPTURE":
        return camera.capture()
    elif command == "HELP":
        return "Commands: forward, backward, left, right, stop, status, photo"
    else:
        return "I did not understand that command."
    return "OK:" + command
