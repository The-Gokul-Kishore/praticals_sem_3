import numpy as np
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt
#step 1 : data preperation

np.random.seed(42)
x = np.linspace(0,10,100)
y = np.sin(x) + np.random.normal(scale=0.5,size = x.shape)

plt.scatter(x,y,label = 'data')

span = 0.3

k = int(span*len(x))

model = KNeighborsRegressor(n_neighbors = k,weights  = 'distance')
x_reshaped = x.reshape(-1,1)
model.fit(x_reshaped,y)
y_pred = model.predict(x_reshaped)

y_pred = model.predict(x_reshaped)

plt.plot(x,y_pred,color = 'orange',label='loess curve')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()