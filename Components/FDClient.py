from FD import FixedDeposit
from Scheme import Scheme
from Scheme import Gscheme
from Scheme import Dscheme



print("Interest and FD Part");
xscheme=Gscheme();
fd1=FixedDeposit(5000,3,xscheme);
print("fd1 interest=",fd1.interest());
yscheme=Dscheme();
fd2=FixedDeposit(7000,3,yscheme);
print("fd2 interest=",fd2.interest());
