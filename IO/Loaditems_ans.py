from pickle import dump,load
from ReadItems_ans import LineItem

f=open("items.bin",'rb')
items=load(f);
f.close();

for x in items:
    print("item id:",x.getID()," Name:",x.getName()," Price:",x.getPrice()," Qty:",x.getQty()," Item total:",x.getItemTotal() )


print(" printing costly items");
newlist=list(filter(lambda q: int(q.getPrice())>3000,items));
for y in newlist:
        print("item id:",y.getID()," Name:",y.getName()," Price:",y.getPrice()," Qty:",y.getQty()," Item total:",y.getItemTotal() )

#for x in items:
#    mylist=[x.getID(),x.getName(),x.getPrice(),x.getQty(),x.getItemTotal()]
#    newlist=list(filter(lambda q: (int(x.getPrice())>3000),mylist));
#    print(newlist);

#for x in items:
#    k=x.getName()
#    if k[0]=="B":
#        print("item id:",x.getID()," Name:",x.getName()," Price:",x.getPrice()," Qty:",x.getQty()," Item total:",x.getItemTotal() )

#for x in items:
#    mylist=[x.getID(),x.getName(),x.getPrice(),x.getQty(),x.getItemTotal()]
#    newlist=list(filter(lambda q: (int(x.getQty())>=50),mylist));
#    print(newlist);

for x in items:
    if x.getQty() <10:
        x.getp
