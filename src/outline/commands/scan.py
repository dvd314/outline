from pathlib import Path

from outline.core.scanner import (
    ProjectScanner,
)

from outline.scanners import (
    SCANNERS,
)

from outline.storage.graph_storage import (
    load_graph,
    save_graph,
)


def command_scan() -> None:

    project_root = Path.cwd()

    graph_path = (
        project_root
        / ".outline"
        / "graph.json"
    )

    old_graph = None

    if graph_path.exists():

        old_graph = load_graph(
            graph_path,
        )

    scanner = ProjectScanner(
        scanners=SCANNERS,
    )

    graph = scanner.scan(
        project_root,
    )

    if old_graph is not None:

        old_notes = {
            obj.path: obj.note
            for obj in old_graph.walk()
            if obj.note
        }

        for obj in graph.walk():
            note = old_notes.get(
                obj.path,
            )

            if note:

                obj.note = note

    save_graph(
        graph,
        graph_path,
    )

    print(
        "semantic graph updated",
    )
