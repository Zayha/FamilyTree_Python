from abc import ABC, abstractmethod


class View(ABC):
    @abstractmethod
    def set_presenter(self, presenter):
        pass

    @abstractmethod
    def start(self):
        pass
