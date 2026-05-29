from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SemanticObject:
    name: str
    note: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)

    children: list["SemanticObject"] = field(default_factory=list)

    parent: "SemanticObject | None" = field(
        default=None,
        repr=False,
        compare=False,
    )

    def add_child(self, child: "SemanticObject") -> None:
        child.parent = self
        self.children.append(child)

    @property
    def path(self) -> str:
        parts = []

        current: SemanticObject | None = self

        while current is not None:
            parts.append(current.name)
            current = current.parent

        return "/".join(reversed(parts))
