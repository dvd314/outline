from outline.core.semantic_object import SemanticObject


class SemanticGraph:

    def __init__(self, root: SemanticObject):
        self.root = root

    def walk(self):
        yield from self._walk(self.root)

    def _walk(self, node: SemanticObject):

        yield node

        for child in node.children:
            yield from self._walk(child)

    def find_by_path(
        self,
        path: str,
    ) -> SemanticObject | None:

        parts = path.strip("/").split("/")

        if not parts:
            return None

        if parts[0] != self.root.name:
            return None

        current = self.root

        for part in parts[1:]:

            found = None

            for child in current.children:

                if child.name == part:
                    found = child
                    break

            if found is None:
                return None

            current = found

        return current
