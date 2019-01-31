import os
#print Current working directoty
print ("Current working directoty:", os.getcwd());
#change Current working directoty
os.chdir("C:\\Python\\test5");
print ("Afetr change - Current working directoty:", os.getcwd());
#directoty in Current folder
print("Printing directories in current folder");
print(os.listdir());
print("Make a dir demo3");
os.mkdir("demo3");
print("directories in current folder");
print(os.listdir());
print("rename demo3 to demo4 ");
os.rename('demo3','demo4');
print("directories in current folder");
print(os.listdir());
str=input("press enter to delete directoty demo4");
os.rmdir("demo4"); # for non empty directoty use os.rmtree()
print("directories in current folder");
print(os.listdir());
print("Deleting file a.txt");
os.remove("a.txt");
print("a.txt deleted");
print("directories in current folder");
print(os.listdir());
