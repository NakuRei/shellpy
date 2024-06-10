import abc
import types


class SignalHandler(abc.ABC):
    @abc.abstractmethod
    def handle(self, signum: int, frame: types.FrameType | None):
        pass
