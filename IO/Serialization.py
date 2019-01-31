from pickle import load , dump

class Account:
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
acc1=Account("abc",7000)
print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());
acc1.deposit(1000);
print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());

print("Serializing the Object");
f=open("acc.bin",'wb')
dump(acc1,f);
f.close();
print("acc1 object serialized");
