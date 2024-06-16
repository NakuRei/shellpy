from .clear import Clear
from .echo import Echo
from .exit import Exit


BUILTIN_COMMANDS = {
    "clear": Clear(),
    "echo": Echo(),
    "exit": Exit(),
}
