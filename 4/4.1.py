import numpy as np
import pandas as pd
x=[4,22,20,7,13,12,17,3,1,21]
y=[10,41,36,17,31,35,47,10,5,41]
x1=np.array(x).mean()
y1=np.array(y).mean()
m=0
g=0
k=0
for i in x:
    j=y[k]
    f=(i-x1)*(j-y1)
    g+=f
    s=(i-x1)**2
    m+=s
    k+=1
k=0
h=g/m
l=y1-h*x1
R2=0
n=10
Rse=0
Rse1=0
R2m=0
for xi in x:
    R2m+=(y[k]-y1)**2
    Rse1+= (y[k]-l-h*xi)**2
    k+=1
R2=Rse1/R2m
print(x1,y1,h,l,1-R2)