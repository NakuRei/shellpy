from .echo import Echo
from .exit import Exit


BUILTIN_COMMANDS = {
    "echo": Echo(),
    "exit": Exit(),
}
