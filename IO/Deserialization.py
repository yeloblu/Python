from pickle import load , dump
from Serialization import Account

print("Deserializing the Object");
f=open("acc.bin",'rb');
acc1=load(f);
print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());
acc1.deposit(1000);
print("acct1 name=" ,acc1.getName()," Balance=",acc1.getBalance());
f.close();
print("acc1 object deserialized");
