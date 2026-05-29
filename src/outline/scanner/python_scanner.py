from pathlib import Path
import ast

from outline.core.semantic_object import SemanticObject
from outline.core.graph import SemanticGraph


def scan_project(project_root: Path) -> SemanticGraph:
    project = SemanticObject(
        name=project_root.name,
    )

    for file in project_root.rglob("*.py"):

        if ".venv" in file.parts:
            continue

        if ".outline" in file.parts:
            continue

        module = scan_file(file, project_root)

        project.add_child(module)

    return SemanticGraph(project)


def scan_file(
    file_path: Path,
    project_root: Path,
) -> SemanticObject:

    relative_path = file_path.relative_to(project_root)

    module = SemanticObject(
        name=str(relative_path),
        metadata={
            "kind": "module",
            "source": str(relative_path),
        },
    )

    tree = ast.parse(
        file_path.read_text(
            encoding="utf-8",
        )
    )

    for node in tree.body:

        if isinstance(node, ast.ClassDef):

            module.add_child(
                SemanticObject(
                    name=node.name,
                    metadata={
                        "kind": "class",
                    },
                )
            )

        elif isinstance(
            node,
            ast.FunctionDef | ast.AsyncFunctionDef,
        ):

            module.add_child(
                SemanticObject(
                    name=node.name,
                    metadata={
                        "kind": "function",
                    },
                )
            )

        elif isinstance(
            node,
            ast.AnnAssign,
        ):
            if isinstance(
                node.target,
                ast.Name,
            ):
                module.add_child(
                    SemanticObject(
                        name=node.target.id,
                        metadata={
                            "kind": "global",
                        },
                    )
                )

        elif isinstance(node, ast.Assign):

            for target in node.targets:

                if isinstance(target, ast.Name):

                    module.add_child(
                        SemanticObject(
                            name=target.id,
                            metadata={
                                "kind": "global",
                            },
                        )
                    )

    return module
