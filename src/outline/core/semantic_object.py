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

    def to_dict(
        self,
    ) -> dict:

        return {
            "name": self.name,
            "note": self.note,
            "metadata": self.metadata,
            "children": [
                child.to_dict()
                for child
                in self.children
            ],
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        obj = cls(
            name=data["name"],
            note=data.get(
                "note",
                "",
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
        )

        obj.children = [
            cls.from_dict(
                child,
            )
            for child
            in data.get(
                "children",
                [],
            )
        ]

        return obj
