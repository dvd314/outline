from abc import ABC, abstractmethod

from outline.core.graph import SemanticGraph


class Renderer(ABC):

    @abstractmethod
    def render(
        self,
        graph: SemanticGraph,
    ) -> str:
        pass
