from .builtin import Builtin


class Echo(Builtin):
    def process(self, args: list[str]):
        print(" ".join(args))
