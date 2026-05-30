from outline.commands.init import InitCommand
from outline.commands.inspect import InspectCommand
from outline.commands.note import NoteCommand
from outline.commands.render import RenderCommand
from outline.commands.scan import ScanCommand


COMMANDS = {
    "init": {
        "help": "Initialize outline project",
        "command": InitCommand,
    },
    "scan": {
        "help": "Build semantic graph",
        "command": ScanCommand,
    },
    "inspect": {
        "help": "Return raw json from graph",
        "command": InspectCommand,
    },
    "render": {
        "help": "Render semantic graph",
        "command": RenderCommand,
    },
    "note": {
        "help": "Edit semantic note",
        "command": NoteCommand,
    },
}
