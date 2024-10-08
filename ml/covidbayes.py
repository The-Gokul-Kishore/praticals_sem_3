import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score,confusion_matrix
data = pd.read_csv('D:\\vscode_prgs\\practicals\\ml\\covid.csv')
data['symptom1'] = data['symptom1'].map({'yes': 1, 'no': 0})
data['symptom2'] = data['symptom2'].map({'yes': 1, 'no': 0})
data['health_condition'] = data['health_condition'].map({'none': 0, 'condition1': 1, 'condition2': 2})
x =data.drop('diagnosis',axis=1)
y=data['diagnosis']

x_train , x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state =42)
model = GaussianNB()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
print("accuracy_score:",accuracy)
confusion_matrixs = confusion_matrix(y_test,y_pred)
print("confusion matrix:",confusion_matrixs)
print("\nPlease answer the following questions:")
symptom1 = input("Do you have symptom 1 (yes/no)? ")
symptom2 = input("Do you have symptom 2 (yes/no)? ")
health_condition = input("Do you have any pre-existing health conditions (none/condition1/condition2)? ")

# Step 5: Process User Input
user_input = pd.DataFrame({
    'symptom1': [1 if symptom1.lower() == 'yes' else 0],
    'symptom2': [1 if symptom2.lower() == 'yes' else 0],
    'health_condition': [0 if health_condition.lower() == 'none' else (1 if health_condition.lower() == 'condition1' else 2)]
})

# Prediction
diagnosis = model.predict(user_input)

# Result Display
if diagnosis[0] == 1:
    print("You are likely to have COVID-19. Please seek medical advice.")
else:
    print("You are likely not to have COVID-19, but it's advisable to monitor your symptoms.")