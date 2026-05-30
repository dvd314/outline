from __future__ import annotations

import json
from pathlib import Path

from outline.core.command import Command
from outline.storage.graph_storage import load_graph


class InspectCommand(Command):
    @staticmethod
    def configure_parser(parser) -> None:
        parser.add_argument(
            "path",
            nargs="?",
        )

    def run(self, args) -> None:
        graph = load_graph(
            Path.cwd() / ".outline" / "graph.json",
        )

        if args.path:
            node = graph.find_by_path(
                args.path,
            )

            if node is None:
                print(
                    f"path not found: {args.path}"
                )
                return

            result = node.to_dict()
        else:
            result = graph.to_dict()

        print(
            json.dumps(
                result,
                indent=2,
            )
        )
