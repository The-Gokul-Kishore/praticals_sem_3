from sklearn.datasets import load_iris
iris = load_iris()
print(type(iris))
import pandas as pd
df = pd.DataFrame(data = iris.data , columns = iris.feature_names)
df['target'] = iris.target
print(df.info())
print(df.head())
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

x = df.drop('target',axis=1)
y = df['target']
print(x.head())
print(y.unique)

xtrain , xtest, ytrain,ytest = train_test_split(x,y,test_size = 0.2, random_state = 42)
classifer = KNeighborsClassifier(n_neighbors = 5).fit(xtrain,ytrain)
ypred = classifer.predict(xtest)
i = 0
print ("\n-------------------------------------------------------------------------")
print ('%-25s %-25s %-25s' % ('Original Label', 'Predicted Label', 'Correct/Wrong'))
print ("-------------------------------------------------------------------------")
for label in ytest:
    print ('%-25s %-25s' % (label, ypred[i]), end="")
    if (label == ypred[i]):
        print (' %-25s' % ('Correct'))
    else:
        print (' %-25s' % ('Wrong'))
    i = i + 1
print ("-------------------------------------------------------------------------")
print("\nConfusion Matrix:\n",metrics.confusion_matrix(ytest, ypred))  
print ("-------------------------------------------------------------------------")
print("\nClassification Report:\n",metrics.classification_report(ytest, ypred)) 
print ("-------------------------------------------------------------------------")
print('Accuracy of the classifer is %0.2f' % metrics.accuracy_score(ytest,ypred))
print ("-------------------------------------------------------------------------")
