from Bank import SavingsAccount
from Bank import CurrentAccount
from Bank import JointAccount
from Bank import Teller



acc1=SavingsAccount("abc",5000);
acc2=CurrentAccount("pqr",9000);
acc3=JointAccount("xyz",9500,"ppp");




teller=Teller();
teller.CashierWindow(acc1);
teller.CashierWindow(acc2);
teller.CashierWindow(acc3);

print("Final Tally");
print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());
#acc1.deposit(1000);
print("acct2 name=" ,acc2.getName()," Balance=",acc2.getBalance());
print("acct3 name=" ,acc3.getName()," Balance=",acc3.getBalance());
