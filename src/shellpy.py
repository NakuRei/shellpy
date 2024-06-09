from builtin import BUILTIN_COMMANDS


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
            # TODO: Implement external commands
            print(f"Command not found: {command}")


if __name__ == "__main__":
    main()
