from outline.core.renderer import Renderer
from outline.core.semantic_object import SemanticObject


class TreeRenderer(Renderer):

    def render(
        self,
        graph,
    ) -> str:

        lines = []

        self._render_object(
            graph.root,
            lines,
            0,
        )

        return "\n".join(
            lines,
        )

    def _render_object(
        self,
        obj: SemanticObject,
        lines: list[str],
        depth: int,
    ) -> None:

        lines.append(
            f'{"    " * depth}{obj.name}'
        )

        for child in obj.children:

            self._render_object(
                child,
                lines,
                depth + 1,
            )
