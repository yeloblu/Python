class FixedDeposit:
    def __init__(self,amt,duration,obj):
        self.__principal=amt;
        self.__duration=duration;
        self.__temp=obj;

    def interest(self):
        return self.__principal*self.__duration*self.__temp.rate();

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


xscheme=Gscheme();
fd1=FixedDeposit(5000,3,xscheme);
print("fd1 interest=",fd1.interest());
yscheme=Dscheme();
fd2=FixedDeposit(7000,3,yscheme);
print("fd2 interest=",fd2.interest());
