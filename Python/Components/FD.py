class FixedDeposit:
    def __init__(self,amt,duration,obj):
        self.__principal=amt;
        self.__duration=duration;
        self.__temp=obj;

    def interest(self):
        return self.__principal*self.__duration*self.__temp.rate();
