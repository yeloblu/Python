from abc import ABC, abstractmethod
class Scheme(ABC):
    @abstractmethod
    def rate(self):
        pass;

class Gscheme(Scheme):
    def rate(self):
        return 0.06;

class Dscheme(Scheme):
    def rate(self):
        return 0.07;
