from pathlib import Path

from outline.core.graph import SemanticGraph

from outline.storage.graph_storage import load_graph

from outline.renderers import (
    RENDERERS,
)


def command_render(args) -> None:

    graph = load_graph(
        Path.cwd()
        / ".outline"
        / "graph.json"
    )

    renderer_name = args.renderer

    renderer_info = RENDERERS.get(
        renderer_name,
    )

    if renderer_info is None:

        available = ", ".join(
            RENDERERS.keys(),
        )

        print(
            f"unknown renderer: {renderer_name}"
        )

        print(
            f"available renderers: {available}"
        )

        return

    renderer = (
        renderer_info["renderer"]()
    )

    print(
        renderer.render(
            graph,
        )
    )
