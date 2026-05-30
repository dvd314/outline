from pathlib import Path
import ast

from outline.core.scanner import Scanner
from outline.core.semantic_object import SemanticObject
from outline.core.dataclasses import SourceLocation


class PythonScanner(Scanner):

    file_patterns = [
        "*.py",
    ]

    def scan_file(
        self,
        file_path: Path,
        project_root: Path,
        parent: SemanticObject,
    ) -> None:

        tree = ast.parse(
            file_path.read_text(
                encoding="utf-8",
            )
        )

        source = str(
            file_path.relative_to(
                project_root,
            )
        )

        for node in tree.body:

            semantic_object = self.scan_node(
                node,
                source,
            )

            if semantic_object:

                parent.add_child(
                    semantic_object,
                )

    def scan_node(
        self,
        node: ast.AST,
        source: str,
    ) -> SemanticObject | None:
        
        location = SourceLocation(
            path=source,
            start_line=node.lineno,
            end_line=node.end_lineno,
        )

        if isinstance(
            node,
            ast.ClassDef,
        ):

            semantic_object = self.create_object(
                node.name,
                "class",
                location,
                private=self._is_private(
                    node.name,
                ),
            )

            for child in node.body:

                child_object = self.scan_node(
                    child,
                    source,
                )

                if child_object:

                    semantic_object.add_child(
                        child_object,
                    )

            return semantic_object

        if isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        ):

            semantic_object = self.create_object(
                node.name,
                "function",
                location,
                private=self._is_private(
                    node.name,
                ),
            )

            for child in node.body:

                child_object = self.scan_node(
                    child,
                    source,
                )

                if child_object:

                    semantic_object.add_child(
                        child_object,
                    )

            return semantic_object

        if isinstance(
            node,
            ast.Assign,
        ):

            if len(
                node.targets,
            ) != 1:

                return None

            target = node.targets[0]

            if not isinstance(
                target,
                ast.Name,
            ):

                return None

            return self.create_object(
                target.id,
                "var",
                location,
                private=self._is_private(
                    target.id,
                ),
            )

        if isinstance(
            node,
            ast.AnnAssign,
        ):

            if not isinstance(
                node.target,
                ast.Name,
            ):

                return None

            return self.create_object(
                node.target.id,
                "var",
                location,
                private=self._is_private(
                    node.target.id,
                ),
            )

        return None

    def _is_private(
        self,
        name: str,
    ) -> bool:

        return (
            name.startswith("_")
            and not name.startswith("__")
        )
