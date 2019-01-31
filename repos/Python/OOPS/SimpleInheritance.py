class Human:
    def __init__(self):
        print("Human constructor is called");
    def play(self):
        print("Ancient humans played with stones");

class Man():
    def __init__(self):
        print("Man constructor called");

    def wish(self):
        print("Many says Hello");
    def laugh(self):
        print("Man smiles");
    def play(self):
        print("Man plays cards");

class Boy(Man,Human):
    def __init__(self):
        print("Boy constructor called");
        super(Boy,self).__init__(); #Super calls the first class listed in th inheritance path
    def reads(self):
        print("Boy reads comics");
    def play(self):
        print("Boy plays cricket");
        #super().play();
        #super.play();

def gaming(obj):

    print("Inside gaming room ::",obj );
    obj.play();

obj1=Man();
obj1.wish();
obj1.laugh();
obj1.play();

obj2=Boy();
obj2.reads();
obj2.play();

obj3=Human();

gaming(obj1);
gaming(obj2);
gaming(obj3);
