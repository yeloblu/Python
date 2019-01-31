class Man:
          def __init__(self, mcolor, mht, mwt):
                                               self.__color=mcolor;
                                               self.__ht=mht;
                                               self.__wt=mwt;
          def getColor(self):
                             return(self.__color)
          def setColor(self,value):
                             if ((value=="white") or (value=="black") or (value=="brown")):
                                                                                         self._color=value;
                             else:
                                  print("Invalid Color ", value, " !! not accepted");
          def getHeight(self):
                             return self.__ht;
          def setHeight(self,value):
                                    self.__ht=value;
          def getWeight(self):
                              return self.__wt;
          def setWeight(self,value):
                                    self.__wt=value;
          def eat(self,n):
                          if (n>=2):
                                    self.__wt+=1;
          def play(self,n):
                           if(n>=2):  
                                    self.__wt=self.__wt-1
                                    self.__color=self.__color="Brown";

#instantiating objects of man class
obj1=Man("white",6,60);
obj2=Man("black",7,70);
print("Obj1 color=" ,obj1.getColor()," Weight=" , obj1.getWeight()," Height=", obj1.getHeight());
print("Obj2 color=" ,obj2.getColor()," Weight=" , obj2.getWeight()," Height=", obj2.getHeight());
obj1.eat(3);
obj2.play(3);
print("after 1eat , 2play ");
print("Obj1 color=" ,obj1.getColor()," Weight=" , obj1.getWeight()," Height=", obj1.getHeight());
print("Obj2 color=" ,obj2.getColor()," Weight=" , obj2.getWeight()," Height=", obj2.getHeight());
obj1.setColor("Green");
print("after setting green ");
print("Obj1 color=", obj1.getColor());
