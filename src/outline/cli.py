import argparse

from outline.commands.init import command_init
from outline.commands.scan import command_scan
from outline.commands.render import command_render


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

    render_parser = subparsers.add_parser(
        "render",
        help="Render semantic graph",
    )

    render_parser.add_argument(
        "renderer",
        nargs="?",
        default="tree",
        help="Renderer name",
    )

    args = parser.parse_args()

    match args.command:
        case "init":
            command_init()

        case "scan":
            command_scan()

        case "render":
            command_render(args)


if __name__ == "__main__":
    main()
