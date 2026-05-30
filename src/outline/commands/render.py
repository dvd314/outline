from __future__ import annotations

import json
import sys

from outline.core.command import Command
from outline.renderers import RENDERERS


class RenderCommand(Command):
    @staticmethod
    def configure_parser(parser) -> None:
        render_subparsers = parser.add_subparsers(
            dest="renderer",
            required=True,
        )

        for name, info in RENDERERS.items():
            renderer_cls = info["renderer"]

            renderer_parser = render_subparsers.add_parser(
                name,
                help=info["help"],
            )

            renderer_cls.configure_parser(renderer_parser)

    def run(self, args) -> None:
        renderer_cls = RENDERERS[args.renderer]["renderer"]
        renderer = renderer_cls()

        data = json.load(sys.stdin)

        print(
            renderer.render(
                data,
                args,
            )
        )
