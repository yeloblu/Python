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
		return self.__price*self.__qty;


items=list();
item1=LineItem(1,"bats  ", 5000, 2 );
item2=LineItem(2,"caps  ", 25  , 25);
item3=LineItem(3,"racket", 6000, 3 );

items.append(item1);
items.append(item2);
items.append(item3);

print("Item ID  Name         Price      Qty    Total");

#for obj in items:
#	print("Item ID=",obj.getID()," Name=",obj.getName()," Price=",obj.getPrice()," Qty=",obj.getQty()," Total=",obj.getTotal());

for obj in items:
	print("",obj.getID(),"     ",obj.getName(),"     ",obj.getPrice(),"     ",obj.getQty(),"     ",obj.getItemTotal());
