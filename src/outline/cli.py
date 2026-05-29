import argparse

from outline.commands.init import command_init
from outline.commands.scan import command_scan
from outline.commands.tree import command_tree


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="outline",
        description="Semantic project workflow",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    subparsers.add_parser(
        "init",
        help="Initialize outline project",
    )

    subparsers.add_parser(
        "scan",
        help="Build semantic graph",
    )

    subparsers.add_parser(
        "tree",
        help="Show semantic tree",
    )

    args = parser.parse_args()

    match args.command:
        case "init":
            command_init()

        case "scan":
            command_scan()

        case "tree":
            command_tree()


if __name__ == "__main__":
    main()
