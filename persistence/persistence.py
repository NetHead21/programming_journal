from abc import ABC, abstractmethod


class PersistenceLayer(ABC):
    @abstractmethod
    def create(self, data) -> None:
        raise NotImplemented("Persistence layers must implement a create method")

    @abstractmethod
    def list(self, order_by: str = None):
        raise NotImplemented("Persistence layers must implement a list method")

    # @abstractmethod
    # def edit(self, entry_id: int, data: dict):
    #     raise NotImplemented("Persistence layers must implement a edit method")
    #
    # @abstractmethod
    # def delete(self, entry_id: int):
    #     raise NotImplemented("Persistence layers must implement a delete method")
