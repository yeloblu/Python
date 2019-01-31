# WAP to
# take a input string reverse and print it.

def rev(data):
             for x in data:
                           print("a:",x,data) 

print("Print reverse of a number");
data=input("Enter a string to reverse:")
print(data);

newno=rev(data)
print("b:", newno);

print("end of program");


x:string="abcd"
data=list(x); <<sting to list 
data1=reversed(data);
reverseddata=".join(data1);<<list to string

reversedata=x[::-1] <<slicing
print(reverse data)