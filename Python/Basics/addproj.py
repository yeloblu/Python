import sys
data =sys.argv;
print(data);
# Entire command line including program name is printed.

data1=sys.argv[1:];
#slice and return all rguments except name of the program
print(data1);
total=0;
for x in data1:
              total=total+x;
print("Total=",total);

print("end of program");