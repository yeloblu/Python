class InsufficientFundsError(RuntimeError):
	def __init(self,msg):
                   self.args=msg;

from abc import ABC , abstractmethod

class Account(ABC):
	def __init__(self,mname,amt):
		self.__name=mname;
		self.__balance=amt;
	def getBalance(self):
		return self.__balance;
	def getName(self):
		return self.__name;
	def _setBalance(self,value):
		return self.__balance;
	def deposit(self,amt):
		self.__balance=self.__balance+amt;
	@abstractmethod
	def withdraw(self,amt):
		pass;

class SavingsAccount(Account):
	def __init__(self,mname,amt):
		self.__name=mname;
		self.__balance=amt;
	def getName(self):
		return self.__name;
	def getBalance(self):
		return self.__balance;
	def deposit(self,amt):
		self.__balance=self.__balance+amt;
	def withdraw(self,amt):
		if ((self.__balance-amt)>=500):
			self.__balance=self.__balance-amt;
		else:
			raise InsufficientFundsError("Insufficient Funds to withdraw");

class JointAccount(Account):
	def __init__(self,mname,amt,sname):
		super().__init__(mname,amt);
		self.__sname=sname
		self.__name=mname;
		self.__balance=amt;

	def getName(self):
		return super().getName()+"::"+self.__sname;
	def getBalance(self):
		return self.__balance;
	def deposit(self,amt):
		self.__balance=self.__balance+amt;
	def withdraw(self,amt):
		if ((self.__balance-amt)>=500):
			self.__balance=self.__balance-amt;
		else:
			raise InsufficientFundsError("Insufficient Funds to withdraw");

class CurrentAccount(Account):
	def __init__(self,mname,amt):
		self.__name=mname;
		self.__balance=amt;
	def getName(self):
		return self.__name;
	def getBalance(self):
		return self.__balance;
	def deposit(self,amt):
		self.__balance=self.__balance+amt;
	def withdraw(self,amt):
		self.__balance=self.__balance-amt;
	def trasnsfer(self,amt):
		self._setBalance=self.getBalance-amt;

class Teller():

	def CashierWindow(self,acc):
		y=input("Enter amount")
		x=input("What do you want to do ? d/w:");
		if x=="d":
			print("performing Deposit operation ");
			acc.deposit(float(y));
			print("acct name=" ,acc.getName()," Balance=",acc.getBalance() );

		elif x=="w":
			print("performing Withdrawal");
			try:
				acc.withdraw(float(y));
			except InsufficientFundsError as e:
				print("".join(e.args));
			print("acct name=" ,acc.getName()," Balance=",acc.getBalance() );
		else:
				print("invalid operation");


acc1=SavingsAccount("abc",5000);
acc2=CurrentAccount("pqr",9000);
acc3=JointAccount("xyz",9500,"ppp");


print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());
#acc1.deposit(1000);
print("acct2 name=" ,acc2.getName()," Balance=",acc2.getBalance());
print("acct3 name=" ,acc3.getName()," Balance=",acc3.getBalance());

teller=Teller();
teller.CashierWindow(acc1);
teller.CashierWindow(acc2);
teller.CashierWindow(acc3);
