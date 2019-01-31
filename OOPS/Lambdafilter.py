mylist=[1,5,4,6,8,11,3,12];
print(mylist);
print("Filtering even numbers ");

evenlist=list(filter(lambda x: (x%2==0),mylist));
print(evenlist);
