print("lets reverse a number");

def reverse(x):
              rev=0;
              d=0;
              while(x>0):
                        d=x%10;
                        rev=rev*10+d;
                        x=int(x/10);
              return rev;

y=int(input("Enter a number: "));
print("reverse of ",y, "=",reverse(y) );
print("end of reverse program");

