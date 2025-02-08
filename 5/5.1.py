import numpy as np
import pandas as pd
n=np.array([[1,22,86,0],
[2,78,32,1],
[3,54,50,1],
[4,68,80,0],
[5,18,12,0],
[6,85,48,0],
[7,78,10,0],
[8,50,74,0],
[9,30,95,0],
[10,91,12,0]])
train_data=pd.DataFrame(n,columns=['id','X','Y','Class'],index=[i for i in range(1,len(n)+1)])
X = train_data.drop(['Class','id'], axis=1)
y = train_data['Class'].values.ravel()
print(X)
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3, p=1)
neigh.fit(X, y)
NewObject = [30, 30]
print(neigh.predict([NewObject]),neigh.predict_proba([NewObject]),neigh.kneighbors([NewObject]))
