class Employee:
    def __init__(self,mname,amt):
        self.__name=mname;
        self.__salary=amt;

    def getName(self):
        return self.__name;
    def getSalary(self):
        return self.__salary;
    def netSalary(self):
        raise NotImplementedException;

class Manager(Employee):
    def netSalary(self):
        return self.getSalary()*(1-00.25);
    def PlanProjects(self):
        print("Manager Plans Project");

class Analyst(Employee):
    def netSalary(self):
        return self.getSalary()*(1-00.20+0.10);
    def DesignSystems(self):
        print("Analyst designs systems");

class SalesManager(Employee):
    def netSalary(self):
        return self.getSalary()*(1+0.10);
    def Markets(self):
        print("Salesman Sells");


class ChequePrinter():
    def printCheque(self,emp):
        print("name=" ,emp.getName()," NetSal=", emp.netSalary());


emp1=Manager("abc",700000);
emp2=Analyst("pqr",500000);
emp3=SalesManager("xyz",200000);


print("emp1 name=", emp1.getName()," Sal=",emp1.getSalary());
print("emp2 name=", emp2.getName()," Sal=",emp2.getSalary());
print("emp3 name=", emp3.getName(),"Sal=",emp3.getSalary());

printer=ChequePrinter();
printer.printCheque(emp1);
printer.printCheque(emp2);
printer.printCheque(emp3);

emp4=Employee("xxx",900000);
#printer.printCheque(emp4);
