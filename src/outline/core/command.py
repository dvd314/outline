from abc import ABC, abstractmethod


class Command(ABC):

    @staticmethod
    def configure_parser(
        parser,
    ) -> None:
        pass

    @abstractmethod
    def run(
        self,
        args,
    ) -> None:
        pass
