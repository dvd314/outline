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
            _object_to_dict(graph.root),
            indent=4,
        )
    )


def load_graph(
    path: Path,
) -> SemanticGraph:

    data = json.loads(
        path.read_text()
    )

    root = _dict_to_object(data)

    return SemanticGraph(root)


def _object_to_dict(
    obj: SemanticObject,
) -> dict:

    return {
        "name": obj.name,
        "note": obj.note,
        "metadata": obj.metadata,
        "children": [
            _object_to_dict(child)
            for child in obj.children
        ],
    }


def _dict_to_object(
    data: dict,
) -> SemanticObject:

    obj = SemanticObject(
        name=data["name"],
        note=data.get("note", ""),
        metadata=data.get(
            "metadata",
            {},
        ),
    )

    for child in data.get(
        "children",
        [],
    ):
        obj.add_child(
            _dict_to_object(child)
        )

    return obj
