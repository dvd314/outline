from pathlib import Path


def command_scan() -> None:
    outline_dir = Path.cwd() / ".outline"

    if not outline_dir.exists():
        print("outline: project not initialized")
        return

    print("scan not implemented yet")
