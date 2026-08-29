from abc import ABC, abstractmethod

class Updateable:
    @abstractmethod
    def Update(self) -> None:
        pass