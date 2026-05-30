from __future__ import annotations

import os
import shlex
import subprocess
import tempfile
from pathlib import Path

from outline.core.command import Command
from outline.storage.graph_storage import load_graph, save_graph


class NoteCommand(Command):
    @staticmethod
    def configure_parser(parser) -> None:
        parser.add_argument(
            "path",
        )

    def run(self, args) -> None:
        graph_path = Path.cwd() / ".outline" / "graph.json"

        graph = load_graph(
            graph_path,
        )

        obj = graph.find_by_path(
            args.path,
        )

        if obj is None:
            print(
                f"path not found: {args.path}"
            )
            return

        editor = os.environ.get("EDITOR") or "nano"
        editor_cmd = shlex.split(editor)

        with tempfile.NamedTemporaryFile(
            mode="w+",
            suffix=".md",
        ) as tmp:
            tmp.write(obj.note)
            tmp.flush()

            subprocess.run(
                editor_cmd + [tmp.name],
                check=True,
            )

            tmp.seek(0)
            obj.note = tmp.read()

        save_graph(
            graph,
            graph_path,
        )
