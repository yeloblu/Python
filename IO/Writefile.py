f=open("test.txt",'a');
s="";
while(not(s=="bye bye")):
    s=input("enter data : ");
    f.write(s);
    #f.write(s+'\n');

print("test file appended");
