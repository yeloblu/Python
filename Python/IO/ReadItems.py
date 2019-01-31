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
	def ItemTotal(self):
		return __price*__qty;
f=open("Items.txt");
print("Item List file open");
#f.seek(0);
#print(f.readline());
items=list();
q=""
#while(not(q=="q")):
    #mylist=[(f.readline())]
#	k=str(f.readline());
	#mylist=[str((f.readline()))];
#	print("list:",k);
#	item1=LineItem(k);
#	break;
    #print(list);
    #newlist=list(map(,mylist));
    #item1=LineItem(1,"bats  ", 5000, 2 );
    #items.append(item1);
    #q=input("press q to quit or n to import new item ");

k=str(f.readline());
args=k.split(',');
for w in args:
             print(w);

item1=LineItem(args[0],args[1],args[2],args[3]);
items.append(item1);

for obj in items:
	print("",obj.getID(),"     ",obj.getName(),"     ",obj.getPrice(),"     ",obj.getQty(),"     ",obj.ItemTotal());
