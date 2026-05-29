import json

from outline.core.renderer import Renderer


class JsonRenderer(Renderer):

    def render(
        self,
        graph,
    ) -> str:

        return json.dumps(
            graph.to_dict(),
            indent=4,
        )
