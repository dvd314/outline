from dataclasses import dataclass

@dataclass(slots=True)
class SourceLocation:
    path: str
    start_line: int
    end_line: int

    start_column: int | None = None
    end_column: int | None = None
