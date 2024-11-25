from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, data: dict):
        raise NotImplemented("Commands must implement an execute method.")
