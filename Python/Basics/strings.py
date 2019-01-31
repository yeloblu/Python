# working with strings in python

print("welcome to strings demo");
x=input("Enter a name:", );

print("name is=", x );
print("upper case of name is=" , x.upper());
print("lower case of name is=" , x.lower());
print("length of char is=" , len(x));
print("no of times a occurs is=" , x.count("a"));
print("First 3 letters in name are=" , x[0:3]);
print("Last 3 letters in name are=" , x[-3:]);
print("Is name upper case ?:", x.isupper());
print("Is name lower case ?:", x.islower());
print("Is name digit ?:", x.isdigit());
print("Is name alphanumeric ?:", x.isalpha());
print("position of first instanceof letter a is=", x.index('a'));
print("Splitting of words");
str="Hello how are you";
args=str.split(' ');
for w in args:
             print(w);

data=list(x);
print(data);
#to join all letters into a single string
print(' '.join(data));
print("End of program");
