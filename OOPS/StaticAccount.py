class InsufficientFundsError(RuntimeError):
	def __init(self,msg):
                   self.args=msg;


class Account:
	counter=0;
	def __init__(self,mname,amt):
		self.__name=mname;
		self.__balance=amt;
		Account.counter=Account.counter+1;

	def getBalance(self):
		return self.__balance;
	def getName(self):
		return self.__name;

	def deposit(self,amt):
		self.__balance=self.__balance+amt;
	def withdraw(self,amt):
		if ((self.__balance-amt)>=500):
			self.__balance=self.__balance-amt;
		else:
			raise InsufficientFundsError("Insufficient Funds to withdraw");

acc1=Account("abc",7000);
print("No of accounts : ", Account.counter);
acc2=Account("pqr",8000);
print("No of accounts : " ,Account.counter);
acc3=Account("xyz",9000);
print("No of accounts : " ,acc3.counter);
