import json
import sys
from outline.core.graph import SemanticGraph

from outline.renderers import (
    RENDERERS,
)


def command_render(args) -> None:

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

    data = json.load(
        sys.stdin,
    )

    renderer = (
        renderer_info["renderer"]()
    )

    print(
        renderer.render(
            data,
        )
    )
