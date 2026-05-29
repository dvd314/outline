from pathlib import Path

from outline.storage.graph_storage import (
    load_graph,
)


def command_tree() -> None:

    graph_file = (
        Path.cwd()
        / ".outline"
        / "graph.json"
    )

    if not graph_file.exists():

        print(
            "outline: graph not found"
        )

        return

    graph = load_graph(
        graph_file
    )

    _print_node(
        graph.root,
        0,
    )


def _print_node(
    node,
    depth,
) -> None:

    print(
        "    " * depth
        + node.name
    )

    for child in node.children:

        _print_node(
            child,
            depth + 1,
        )
