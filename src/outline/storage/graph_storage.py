import json
from pathlib import Path

from outline.core.graph import SemanticGraph
from outline.core.semantic_object import SemanticObject


def save_graph(
    graph: SemanticGraph,
    path: Path,
) -> None:

    path.write_text(
        json.dumps(
            graph.to_dict(),
            indent=4,
        )
    )


def load_graph(
    path: Path,
) -> SemanticGraph:

    return SemanticGraph.from_dict(
        json.loads(
            path.read_text(),
        )
    )
