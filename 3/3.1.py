import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
data= pd.read_csv('7_36 (1).csv', delimiter=";", header=None)
X = data.to_numpy() #Объекты
print(X[0])
plt.imshow(X[0].reshape([2,5]), cmap='Greys_r')
pca = PCA(n_components=10, svd_solver='full') #Создание объекта класса PCA. В качестве параметров выступает количество ГК и метод оптимизации
X_transformed = pca.fit(X).transform(X) #X_transformed -- ndarray объектов, где каждый объект описывается двумя ГК
print(X_transformed[0])
plt.scatter(X_transformed[:61, 0], X_transformed[:61, 1], edgecolor='none', s=40)
plt.show()
explained_variance = np.round(np.cumsum(pca.explained_variance_ratio_),3)
print(explained_variance)
plt.plot(np.arange(10), explained_variance, ls = '-')
plt.show()