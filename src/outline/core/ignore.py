from pathlib import Path
from fnmatch import fnmatch


class IgnoreMatcher:

    def __init__(
        self,
        project_root: Path,
    ):

        self.patterns = []

        self._load(
            project_root
        )

    def _load(
        self,
        project_root: Path,
    ) -> None:

        ignore_file = (
            project_root
            / ".outlineignore"
        )

        if not ignore_file.exists():
            return

        for line in (
            ignore_file.read_text()
            .splitlines()
        ):

            line = line.strip()

            if (
                not line
                or line.startswith("#")
            ):
                continue

            self.patterns.append(
                line
            )

    def is_ignored(
        self,
        path: str,
    ) -> bool:

        parts = path.split("/")

        for pattern in self.patterns:

            if fnmatch(
                path,
                pattern,
            ):
                return True

            if pattern in parts:
                return True

        return False
