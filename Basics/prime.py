print("Prime no");

x=int(input("Enter a no:"));
flag=1;

if (x>1):
        for i in range (2,(x//2)+1):
                                 if (x%i==0):
                                             flag=0;
				 

if (flag==0):
             print(x, " no is not a prime");
else :
      print(x, " no is prime");

if (x<1):
         print("invalid input");