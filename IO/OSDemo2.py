import os
#to recurese through directory after directoty using walk
for file in os.walk("C:\\Python"):
    print(file);

#check if name given is file or directoty
print("hello.txt is a file=", os.path.isfile("C:\\Python\\IO\\hello.txt"));
print("test5 is a file=", os.path.isfile("C:\\Python\\IO\\test5"));

#to check if file or directoty exists
print("Does hello.txt exist ?: ", os.path.exists("C:\\Python\\IO\\hello.txt"));
print("Does atul.txt exist ?: ", os.path.exists("C:\\Python\\IO\\atul.txt"));
print("Does test10 exist ?: ", os.path.exists("C:\\Python\\IO\\test10"));
try :
    os.mkdir("test5");
    print("directoty creted sucessfully");
except OSError as e:
    print(e);
print("directories in current folder");
print(os.listdir());
