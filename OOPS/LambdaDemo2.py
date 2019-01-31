class Test:
    def __init__(self,name):
        self.name=name;
    def attach(self,f):
        self.f=f;
    def invoke(self):
        self.f(self.name);
#class Hello:

def sayhello(x):
        print("hello says ",x);

obj1=Test("abc");
obj1.attach(sayhello);
obj1.invoke();
obj2=Test("pqr");
obj2.attach(lambda x:print("see n says",x));
obj2.invoke();
obj3=Test("atul");
obj3.attach(sayhello);
obj4=Test("xyz");
obj4.attach(lambda x:print("Bye Bye", x));
users=list();
users.append(obj1);
users.append(obj2);
users.append(obj3);
users.append(obj4);

for temp in users:
    temp.invoke();
