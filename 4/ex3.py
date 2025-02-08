import numpy as np

x=[13,4,11,20]
y=[8,5,6,15]
x1=np.array(x).mean()
y1=np.array(y).mean()
k=0
R2=0
n=4
Rse=0
Rse1=0
R2m=0
o1=0.6307692307692307
o0=0.930769230769231
for xi in x:
    R2m+=(y[k]-y1)**2
    Rse1+= (y[k]-o0-o1*xi)**2
    k+=1
Rse=np.sqrt(1/(n-2)*Rse1)
R2=Rse1/R2m
print(1-R2,Rse)