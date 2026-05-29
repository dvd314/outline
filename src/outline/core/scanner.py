from abc import ABC, abstractmethod
from fnmatch import fnmatch
from pathlib import Path

from outline.core.graph import SemanticGraph
from outline.core.ignore import IgnoreMatcher
from outline.core.semantic_object import SemanticObject


class Scanner(ABC):

    file_patterns: list[str] = []

    @abstractmethod
    def scan_file(
        self,
        file_path: Path,
        project_root: Path,
        parent: SemanticObject,
    ) -> None:
        pass

    def create_object(
        self,
        name: str,
        kind: str,
        source: str,
        private: bool,
    ) -> SemanticObject:

        return SemanticObject(
            name=name,
            metadata={
                "kind": kind,
                "source": source,
                "private": private,
            },
        )



class ProjectScanner:

    def __init__(
        self,
        scanners: list[Scanner],
    ):

        self.scanners = scanners

    def scan(
        self,
        project_root: Path,
    ) -> SemanticGraph:

        project = SemanticObject(
            name=project_root.name,
            metadata={
                "kind": "project",
            },
        )

        ignore = IgnoreMatcher(
            project_root,
        )

        directories: dict[str, SemanticObject] = {
            "": project,
        }

        for file in project_root.rglob("*"):

            if not file.is_file():
                continue

            relative_path = str(
                file.relative_to(
                    project_root,
                )
            )

            if ignore.is_ignored(
                relative_path,
            ):
                continue

            scanner = self._find_scanner(
                file,
            )

            if scanner is None:
                continue

            parent = self._get_parent_directory(
                relative_path,
                directories,
                project,
            )

            scanner.scan_file(
                file,
                project_root,
                parent,
            )

        return SemanticGraph(
            project,
        )

    def _find_scanner(
        self,
        file: Path,
    ) -> Scanner | None:

        for scanner in self.scanners:

            for pattern in scanner.file_patterns:

                if fnmatch(
                    file.name,
                    pattern,
                ):
                    return scanner

        return None

    def _get_parent_directory(
        self,
        relative_path: str,
        directories: dict[str, SemanticObject],
        project: SemanticObject,
    ) -> SemanticObject:

        parent = project

        current_path = ""

        parts = Path(
            relative_path,
        ).parts[:-1]

        for part in parts:

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
                    directory,
                )

                directories[
                    current_path
                ] = directory

            parent = directories[
                current_path
            ]

        return parent
