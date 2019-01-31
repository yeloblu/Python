f=open("hello.txt");
print(f.read());
print("Go to start of the file");
f.seek(0);
print("read only 1st line");
print(f.readline());
print("readfile entire line by line");
for line in f:
    print(line);

print("read first 3 lines");
counter=0;
f.seek(0);
print("before:", counter);
for line in f:
    #print("before1:", counter);
    if counter>2:
        break;

    print(line);
    #print(counter);
    counter+=1;
