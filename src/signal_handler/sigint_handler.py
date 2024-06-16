import os
import signal
import types


from .signal_handler import SignalHandler


class SigIntHandler(SignalHandler):
    def __init__(self, shell_prompt: str) -> None:
        super().__init__()
        self._pid: int | None = None
        self._shell_prompt = shell_prompt

    def set_pid(self, pid: int | None):
        self._pid = pid

    def handle(self, signum: int, frame: types.FrameType | None):
        if self._pid is not None:
            try:
                os.kill(self._pid, signal.SIGINT)
            except ProcessLookupError:
                print("Process already exited or invalid PID")
            except Exception as e:
                print(f"Error sending SIGINT to process {self._pid}: {e}")
            finally:
                self._pid = None  # Reset PID after sending signal

            print("\n", end="", flush=True)
        else:
            print(f"\n{self._shell_prompt}", end="", flush=True)
