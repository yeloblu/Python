class student:
    def __init__(self,mname,mage,mark1,mark2,mark3,mark4,mark5):
        self.__name=mname;
        self.__age=mage;
        self.__mark1=mark1;
        self.__mark2=mark2;
        self.__mark3=mark3;
        self.__mark4=mark4;
        self.__mark5=mark5;


    def getName(self):
        return self.__name;
    def getAge(self):
        return self.__age;
    def getMark1(self):
        return self.__mark1;
    def getMark2(self):
        return self.__mark2;
    def getMark3(self):
        return self.__mark3;
    def getMark4(self):
        return self.__mark4;
    def getMark5(self):
        return self.__mark5;
    def getTotal(self):
        return self.__mark1+ self.__mark2 + self.__mark3 + self.__mark4 + self.__mark5 ;

    def setName(self,value):
        self.__name=value;
    def setAge(self,value):
        self.__age=value;
    def setMark1(self,value):
        self.__mark1=value;
    def setMark2(self,value):
        self.__mark2=value;
    def setMark3(self,value):
        self.__mark3=value;
    def setMark4(self,value):
        self.__mark4=value;
    def setMark5(self,value):
        self.__mark5=value;

    def calGrade(self,total):
        if total < 200:
            grade="Fail";
            return grade;
        elif  (total > 200 and total < 300):
            grade="Second class";
            return grade;
        elif ( ( total >= 300) and (total < 349)):
            grade="First class";
            return grade;
        elif  total >= 350:
            grade="Distinction";
            return grade;




items=list();
item1=student("ABC  ", 23 ,61,57,59,55,87);
item2=student("PQR  ", 24 ,90,89,59,60,82);
item3=student("XYZ  ", 25 ,23,34,38,29,33);

items.append(item1);
items.append(item2);
items.append(item3);

print("Name         Age     Science  Math    History  Geography English   Total     Grade ");
for obj in items:
	print("",obj.getName(),"     ",obj.getAge(),"     ",obj.getMark1(),"     ",obj.getMark2(),"     ",obj.getMark3(),"     ",obj.getMark4(),"     ",obj.getMark5(),"     ",obj.getTotal(), "     ",obj.calGrade(obj.getTotal()));
