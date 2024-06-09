import abc


class Builtin(abc.ABC):
    @abc.abstractmethod
    def process(self, args: list[str]):
        pass
