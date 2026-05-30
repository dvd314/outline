from __future__ import annotations

import argparse

from outline.commands import COMMANDS


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="outline",
        description="Semantic project workflow",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    for name, info in COMMANDS.items():
        command_cls = info["command"]

        command_parser = subparsers.add_parser(
            name,
            help=info["help"],
        )

        command_cls.configure_parser(command_parser)

    args = parser.parse_args()

    command_cls = COMMANDS[args.command]["command"]
    command = command_cls()

    command.run(args)


if __name__ == "__main__":
    main()
