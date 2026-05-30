from pathlib import Path
import os
import tempfile
import subprocess

from outline.storage.graph_storage import (
    load_graph,
    save_graph,
)


def command_note(args) -> None:

    graph_path = (
        Path.cwd()
        / ".outline"
        / "graph.json"
    )

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

    editor = (
        os.environ.get("EDITOR")
        or "nano"
    )

    with tempfile.NamedTemporaryFile(
        mode="w+",
        suffix=".md",
    ) as tmp:

        tmp.write(
            obj.note,
        )

        tmp.flush()

        subprocess.run(
            [editor, tmp.name],
            check=True,
        )

        tmp.seek(0)

        obj.note = tmp.read()

    save_graph(
        graph,
        graph_path,
    )
