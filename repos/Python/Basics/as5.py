# WAP to
# take a input number and check if it is a prime number or not


def checkPrime(data): 
    for i in range(2,int(data//2+1)):
        if (data % i)== 0:
              #print(data, " This is not a prime no");
              flag=0;
#        else :
#              #print(data, " This is a prime no");
#              flag=1;
#    else: 
#        print(data, " This is not a prime no");
#         flag=1;

print("Program to check prime no");
data=int(input("Input no and check if it is a prime:"));
flag=0;
checkPrime(data) 
if(flag==0):
            print(data, " This is not a prime no");
else:
     print(data, " This is a prime no");
if data<1:
          print(data, " is invaid input");
print("End of program");
