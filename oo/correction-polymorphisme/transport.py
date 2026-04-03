from abc import ABC, abstractmethod

class Transport(ABC):

    @abstractmethod
    def se_deplacer(self):
        pass