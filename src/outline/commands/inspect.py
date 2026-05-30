from pathlib import Path
import json

from outline.storage.graph_storage import (
    load_graph,
)

def command_inspect(args) -> None:

    graph = load_graph(
        Path.cwd()
        / ".outline"
        / "graph.json"
    )

    result = "empty"

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
