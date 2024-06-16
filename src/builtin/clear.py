from .builtin import Builtin


class Clear(Builtin):
    def process(self, args: list[str]):
        print("\033[H\033[2J\033[3J", end="")
