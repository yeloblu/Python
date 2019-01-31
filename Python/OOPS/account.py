class InsufficientFundsError(RuntimeError):
	def __init(self,msg):
                   self.args=msg;


class Account:
	def __init__(self,mname,amt):
		self.__name=mname;
		self.__balance=amt;

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
acc2=Account("pqr",9000);

print("acct name=" ,acc1.getName()," Balance=",acc1.getBalance() );
acc1.deposit(1000);
print("acct name=" ,acc1.getName()," Balance=",acc1.getBalance() );
amt=input("Input amt to withdraw:");
try:
	acc1.withdraw(float(amt));
except InsufficientFundsError as e:
	print("".join(e.args));

print("acct name=" ,acc1.getName()," Balance=",acc1.getBalance() );
		