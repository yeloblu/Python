Dict={'abc':18,'atul':23,'alex':45,'jones':53}
print(Dict);
print((Dict['alex']));

Dict.update({'atul':25});
print(Dict);
print("Deleting Keys from Python");
#del Dict['charlie'];
print(Dict);

print("items method returns key value by tuple");

print(list(Dict.items()));
Boys={'scott':44,'abc':18};
print("Check if given key exists in dictionary")
man={'abc':18};

for key in list (Dict.keys()):
    if key in list (Boys.keys()):
        print("key found in boys collection");
    else:
        print("Key not found");

print("Sorting the dictionary");

Managers=list(Dict.keys());
Managers.sort();
for s in Managers:
    print(":".join((s,str(Dict[s]))));
print("Length of dict:" ,len(Dict));
print("Printable String:", str(Dict));
