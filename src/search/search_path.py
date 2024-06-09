import os


def search_path(command: str):
    if "/" in command:
        if os.path.exists(command) and os.path.isfile(command):
            return command
        return None

    for dir_path in os.environ["PATH"].split(":"):
        command_path = os.path.join(dir_path, command)
        if os.path.exists(command_path) and os.path.isfile(command_path):
            return command_path
    return None
