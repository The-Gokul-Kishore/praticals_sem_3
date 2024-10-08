import pandas as pd
from   sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score,precision_score,recall_score,confusion_matrix

data = {
    'document':[
        "Sky is blue",
        "the sun is bright",
        "the sun in the blue sky",
        "We can see the shining sun , the bright sun",
        "The quick brown fox jumps over the lazy dog",
        "The dog is lazy but cute",
        "the dog is fast when not lazy",
        "the weather is nice when it is sunny and sky is blue"
    ],
    'label':['weather','weather','weather','weather',"animal","animal","animal","weather"]
}
df = pd.DataFrame(data)
Vectorizer = TfidfVectorizer()
x = Vectorizer.fit_transform(df['document'])
y = df['label']

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size = 0.3,random_state=42 ,stratify = y)

model  = MultinomialNB()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,average='weighted',zero_division=1)
recall = recall_score(y_true=y_test,y_pred=y_pred,average='weighted',labels=['weather','animal'],zero_division=1)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")

# Optional: Confusion Matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:\n", conf_matrix)