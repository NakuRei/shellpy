from .builtin import Builtin


class Exit(Builtin):
    def process(self, args: list[str]):
        exit(0)
