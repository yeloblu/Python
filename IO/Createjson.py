import json

mydata=["alex","read and write files in json",12345];
f=open("test.json","w");
json.dump(mydata,f);
f.close();
print("json file created");
