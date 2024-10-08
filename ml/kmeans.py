import pandas as pd
import numpy as np
np.random.seed(42)
n_customers = 200
customer_ids = np.arange(1,n_customers+1)
genders = np.random.choice(['Male','Female'],size = n_customers)
ages    = np.random.randint(18,70,size= n_customers)
annual_incomes = np.random.randint(20,150,size= n_customers)
spending_scores  = np.random.randint(1,101,size = n_customers)

df = pd.DataFrame({
    'customer_id':customer_ids,
    'gender':genders,
    'age':ages,
    'annual_income':annual_incomes,
    "spending_scores":spending_scores
})

import matplotlib.pyplot as plt
import seaborn as sns
import re 
from sklearn.cluster import KMeans
#
"""plt.figure(figsize=(10,10))
sns.histplot(df,x='annual_income',hue='gender',multiple="stack")
plt.title("annual income with respect to gender")
plt.grid()
plt.figure(figsize=(20,15))
sns.countplot(data=df,x='age')

plt.figure(figsize=(8,8))

df.gender.value_counts().plot(kind="pie",autopct="%.2f%%",shadow=True,explode=(0,0.04))
plt.legend()
plt.show()"""
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])
df.head()
df.drop("customer_id",axis=1,inplace=True)
df.head()
p = []
for i in range(1, 11):
    Kmodel = KMeans(n_clusters=i,n_init=15,max_iter=500)
    Kmodel.fit(df)
    p.append(Kmodel.inertia_)
plt.plot(range(1,11),p,marker='o')
plt.title("elbow curve")
plt.grid()

plt.show()
Kmodel = KMeans(n_clusters=6)
Kmodel.fit_predict(df)
pre = Kmodel.predict(df)
o = Kmodel.cluster_centers_
len(o)
df['cluster']=pre
df.head()
plt.scatter(Kmodel.cluster_centers_[:,0],Kmodel.cluster_centers_[:,1],c="green",s=200,alpha=0.5)
from sklearn.metrics import mean_squared_error as mse, r2_score as d
print(mse(df['cluster'],pre))
print(d(df['cluster'],pre))
plt.show()        