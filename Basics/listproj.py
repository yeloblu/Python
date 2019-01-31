names=["Allen","Alex","Scott"];

for x in names:
               print(x);
# Add a name to list
names.append("Bob");
print("After append");
for x in names:
              print(x);
print("to check if Atul exists in list");
if "Atul" in names:
                  print("Atul found in names");
else:
    print("Atul not found in names");

print("No of items in list=",len(names));
print("Add Atul to 2nd position");
names.insert(1,"Atul");
for x in names:
               print(x);
print("Remove Scott from list");
names.remove("Scott");
for x in names:
               print(x);
print("print list in reverse order");
for x in reversed(names):
                        print(x);

print("End of program");