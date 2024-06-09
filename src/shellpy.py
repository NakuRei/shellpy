def main():
    while True:
        line = input("> ")
        tokens = line.split()

        # If no command is given, continue
        if len(tokens) == 0:
            continue

        command = tokens[0]
        args = tokens[1:]

        # TODO: Implement external commands
        print(f"{command=}, {args=}")


if __name__ == "__main__":
    main()
