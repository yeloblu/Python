import json

f=open("test.json");
jsondata=json.load(f);
print(jsondata);
f.close();
