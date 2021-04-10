from abc import ABC, abstractmethod


class Accessory(ABC):
    name: str

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def set_state(self, state: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def get_state(self) -> int:
        raise NotImplementedError()

    def handler(self, payload):
        self.set_state(payload)
