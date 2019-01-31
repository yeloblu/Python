f=open("ItemList.txt",'a');
print("Item List file open");
#f.seek(0);
serialno=1
q=""
#take all inputs add commas later
#infinite loop , q to quit n for new item
while(not(q=="q")):
     s=input("Enter name of Item : ");
     f.write(str(serialno));
     f.write(",")
     f.write(s);
     f.write(",")
     s=input("Enter rate of Item : ");
     f.write(s);
     f.write(",")
     s=input("Enter qty of Item : ");
     f.write(str(s)+'\n');
     serialno+=1
     q=input("press q to quit or n for new item ");
     s="";
