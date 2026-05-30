from outline.core.renderer import Renderer
from outline.core.semantic_object import SemanticObject


class TreeRenderer(Renderer):

    @staticmethod
    def configure_parser(
        parser,
    ) -> None:

        parser.add_argument(
            "-L",
            "--depth",
            type=int,
            default=999,
        )

    def render(
        self,
        obj: dict,
        args,
    ) -> str:

        lines = []

        self._render_object(
            obj,
            lines,
            0,
            args.depth,
        )

        return "\n".join(
            lines,
        )

    def _render_object(
        self,
        obj: dict,
        lines: list[str],
        depth: int,
        max_depth: int,
    ) -> None:

        lines.append(
            f'{"    " * depth}{obj["name"]}'
        )

        if depth + 1 > max_depth:
            return

        for child in obj["children"]:

            self._render_object(
                child,
                lines,
                depth + 1,
                max_depth,
            )
