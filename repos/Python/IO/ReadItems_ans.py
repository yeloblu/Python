from pickle import dump,load
class LineItem:
	def __init__(self,mno,mname,mprice,mqty):
		self.__no=mno;
		self.__name=mname;
		self.__price=mprice;
		self.__qty=mqty

	def setID(self,value):
		self.__no=value;
	def setName(self,value):
		self.__name=value;
	def setPrice(self,value):
		self.__price=value
	def setQty(self,value):
		self.__qty=value;

	def getID(self):
		return self.__no;
	def getName(self):
		return self.__name;
	def getPrice(self):
		return self.__price;
	def getQty(self):
		return self.__qty;
	def getItemTotal(self):
		return int(self.__price)*int(self.__qty);
f=open("Items.txt");
print("Item List file open");
items=list();
for line in f:
    try:
        args=line.split(',');
        item1=LineItem(args[0],args[1],args[2],args[3]);
        items.append(item1);
    except:
        pass;
f.close();
f1=open("items.bin",'wb');
dump(items,f1)
f1.close();
print("items file serialized to items.bin");
