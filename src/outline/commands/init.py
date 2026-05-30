from __future__ import annotations

from pathlib import Path

from outline.core.command import Command


OUTLINE_DIR = ".outline"


class InitCommand(Command):
    def run(self, args) -> None:
        outline_dir = Path.cwd() / OUTLINE_DIR

        if outline_dir.exists():
            print("outline: already initialized")
            return

        outline_dir.mkdir()
        (outline_dir / "cache").mkdir()
        (outline_dir / "generated").mkdir()

        print(f"initialized: {outline_dir}")
