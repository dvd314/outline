from pathlib import Path


def command_tree() -> None:
    outline_dir = Path.cwd() / ".outline"

    if not outline_dir.exists():
        print("outline: project not initialized")
        return

    print("tree not implemented yet")
