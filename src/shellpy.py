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

        # If the command is a builtin command, execute it
        if command in BUILTIN_COMMANDS:
            BUILTIN_COMMANDS[command].process(args)
        else:
            command_path = search_path(command)
            if command_path is None:
                print(f"shellpy: {command}: command not found", file=sys.stderr)
                continue

            # TODO: Implement the execution of external commands
            print(f"Executing {command_path} with args {args}")


if __name__ == "__main__":
    main()
