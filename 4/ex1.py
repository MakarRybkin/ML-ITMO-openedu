import numpy as np
import pandas as pd
x=[13,4,11,20]
y=[8,5,6,15]
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
h=g/m
l=y1-h*x1
print(x1,y1,h,l)