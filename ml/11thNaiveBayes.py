import pandas as pd
from sklearn.metrics import f1_score,confusion_matrix,accuracy_score,auc,roc_curve
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

data = pd.read_csv("D:\\vscode_prgs\\practicals\\ml\\11thone.csv")
y = data['class']
x= data.drop('class',axis =1)
print(y)
print(x)

x_train , x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state = 42)

model = GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy_score:{accuracy:.2f}")

conf_matrix = confusion_matrix(y_test,y_pred)

print("confusion matrix \n",conf_matrix)

f1 = f1_score(y_test,y_pred,pos_label='yes')

print(f"f1 score:{f1:.2f}")

y_test_bin = y_test.map({'yes':1,'no':0})
y_pred_prob = model.predict_proba(x_test)[:,1]
fpr,tpr ,thresholds = roc_curve(y_test_bin,y_pred_prob)
roc_auc= auc(fpr,tpr)

plt.figure()
plt.plot(fpr,tpr,color  ="Blue",lw=2,label =f"roc curev(auc= {roc_auc:.2f})" )
plt.plot([0,1],[0,1],linestyle='--',color = 'gray')
plt.xlabel('false postive rate')
plt.ylabel('true postive rate')
plt.title('ROC curve')
plt.legend(loc = "lower right")
plt.show()