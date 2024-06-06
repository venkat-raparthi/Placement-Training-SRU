from abc import ABC, abstractmethod

class Authentiction(ABC):
    def __init__(self,password,attempts):
        self.password=password
        self.attempts=attempts

    @abstractmethod
    def display_password(self):
        pass