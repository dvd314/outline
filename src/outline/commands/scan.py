from pathlib import Path

from outline.scanner.python_scanner import (
    scan_project,
)
from outline.storage.graph_storage import (
    save_graph,
)


def command_scan() -> None:

    project_root = Path.cwd()

    outline_dir = (
        project_root / ".outline"
    )

    if not outline_dir.exists():

        print(
            "outline: project not initialized"
        )

        return

    graph = scan_project(
        project_root
    )

    save_graph(
        graph,
        outline_dir / "graph.json",
    )

    print(
        "semantic graph updated"
    )
