from pathlib import Path

from outline.core.scanner import (
    ProjectScanner,
)

from outline.scanners import (
    SCANNERS,
)

from outline.storage.graph_storage import save_graph

def command_scan() -> None:

    project_root = Path.cwd()

    scanner = ProjectScanner(
        scanners=SCANNERS,
    )

    graph = scanner.scan(
        project_root,
    )

    save_graph(
        graph,
        project_root
        / ".outline"
        / "graph.json",
    )

    print(
        "semantic graph updated",
    )
