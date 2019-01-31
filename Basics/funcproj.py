def addition(x,y):
                 return x+y;
def totsum(data):
                total=0;
                for x in data:
                             total=total+x;
                return total;

print("Welcome to addition prog");
result=addition(10,20)
print("Addition of 10 and 20=",result);
result1=totsum([10,20,30,40]);
print("Addition of 10 , 20 , 30 , 40 =",result1);

print("End of program");