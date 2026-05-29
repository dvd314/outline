from pathlib import Path
import ast

from outline.core.graph import SemanticGraph
from outline.core.semantic_object import SemanticObject


IGNORED_DIRS = {
    ".git",
    ".outline",
    ".venv",
    "__pycache__",
}


def create_object(
    name: str,
    kind: str,
    source: str,
) -> SemanticObject:

    return SemanticObject(
        name=name,
        metadata={
            "kind": kind,
            "source": source,
        },
    )


def scan_project(
    project_root: Path,
) -> SemanticGraph:

    project = SemanticObject(
        name=project_root.name,
        metadata={
            "kind": "project",
        },
    )

    directories: dict[str, SemanticObject] = {
        "": project,
    }

    for file in project_root.rglob("*.py"):

        if any(
            part in IGNORED_DIRS
            for part in file.parts
        ):
            continue

        if file.name == "__init__.py":
            continue

        relative_path = file.relative_to(
            project_root
        )

        parent = project

        current_path = ""

        for part in relative_path.parts[:-1]:

            current_path = (
                f"{current_path}/{part}"
                if current_path
                else part
            )

            if current_path not in directories:

                directory = SemanticObject(
                    name=part,
                    metadata={
                        "kind": "directory",
                    },
                )

                parent.add_child(
                    directory
                )

                directories[
                    current_path
                ] = directory

            parent = directories[
                current_path
            ]

        scan_file(
            file,
            project_root,
            parent,
        )

    return SemanticGraph(
        project
    )


def scan_file(
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
            project_root
        )
    )

    for node in tree.body:

        semantic_object = scan_node(
            node,
            source,
        )

        if semantic_object:

            parent.add_child(
                semantic_object
            )


def scan_node(
    node: ast.AST,
    source: str,
) -> SemanticObject | None:

    if isinstance(
        node,
        ast.ClassDef,
    ):

        semantic_object = create_object(
            node.name,
            "class",
            source,
        )

        for child in node.body:

            child_object = scan_node(
                child,
                source,
            )

            if child_object:

                semantic_object.add_child(
                    child_object
                )

        return semantic_object

    if isinstance(
        node,
        (
            ast.FunctionDef,
            ast.AsyncFunctionDef,
        ),
    ):

        semantic_object = create_object(
            node.name,
            "function",
            source,
        )

        for child in node.body:

            child_object = scan_node(
                child,
                source,
            )

            if child_object:

                semantic_object.add_child(
                    child_object
                )

        return semantic_object

    if isinstance(
        node,
        ast.Assign,
    ):

        if len(node.targets) != 1:
            return None

        target = node.targets[0]

        if not isinstance(
            target,
            ast.Name,
        ):
            return None

        return create_object(
            target.id,
            "global",
            source,
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

        return create_object(
            node.target.id,
            "global",
            source,
        )

    return None
