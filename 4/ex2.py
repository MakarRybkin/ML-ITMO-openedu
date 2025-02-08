import numpy as np
import pandas as pd
x=[13,4,11,20]
y=[8,5,6,15]
x1=np.array(x).mean()
y1=np.array(y).mean()
k=0
m=0
m1=0
n=4
o1=0.6307692307692307
o0=0.930769230769231
for xi in x:
    m+= (y[k] - o0 - (o1 * xi)) ** 2
    m1+= (xi - x1) ** 2
    k+=1
se=np.sqrt(m/(n-2))*np.sqrt((1/n)+((x1**2)/m1))
se2=np.sqrt(m/(n-2))*np.sqrt(1/(m1))
print(se,se2)