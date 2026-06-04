from abc import ABC, abstractmethod

class BackendClient(ABC):

    @abstractmethod
    def login(self, *args, **kwargs):
        pass

    """
    @abstractmethod
    def health(self):
        pass
    """
