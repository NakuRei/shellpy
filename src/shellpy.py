import os
import sys

from builtin import BUILTIN_COMMANDS
from search import search_path


def main():
    while True:
        line = input("> ")
        tokens = line.split()

        # If no command is given, continue
        if len(tokens) == 0:
            continue

        command = tokens[0]
        args = tokens[1:]

        if command in BUILTIN_COMMANDS:
            BUILTIN_COMMANDS[command].process(args)
        else:
            command_path = search_path(command)
            if command_path is None:
                print(f"shellpy: {command}: command not found", file=sys.stderr)
                continue

            pid = os.fork()
            if pid == 0:  # Child process
                os.execv(command_path, [command] + args)
            else:  # Parent process
                os.waitpid(pid, 0)


if __name__ == "__main__":
    main()
