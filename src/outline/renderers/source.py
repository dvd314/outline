from pathlib import Path

from outline.core.semantic_object import (
    SemanticObject,
)

from outline.core.renderer import (
    Renderer,
)


class SourceRenderer(Renderer):

    def render(
        self,
        obj: dict,
        args
    ) -> str:

        location = obj.get("metadata").get(
            "source_location",
        )

        if location is None:

            return ""

        file_path = (
            Path.cwd()
            / location["path"]
        )

        with open(
            file_path,
            encoding="utf-8",
        ) as f:

            lines = f.readlines()

        start_line = (
            location["start_line"]
            - 1
        )

        end_line = (
            location["end_line"]
        )

        return "".join(
            lines[
                start_line:end_line
            ]
        )
