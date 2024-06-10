from .builtin import Builtin


class Exit(Builtin):
    def process(self, args: list[str]):
        print("exit")
        exit(0)
