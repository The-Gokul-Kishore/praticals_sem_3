import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD

#create dem data
np.random.seed(42)

n_users = 1000
n_items = 300


user_ids = np.arange(1,n_users+1)
item_ids = np.arange(1,n_items+1)
n_ratings = 20000
user_column = np.random.choice(user_ids,size=n_ratings,replace=True)
item_column = np.random.choice(item_ids,size=n_ratings,replace=True)
ratings_column = np.random.randint(1,6,size=n_ratings)
ratings_df = pd.DataFrame({'userId':user_column,'itemId':item_column,'rating':ratings_column})
# Option 1: Drop duplicates
ratings_df = ratings_df.drop_duplicates(subset=['userId', 'itemId'])

user_item_matrix =ratings_df.pivot(index='userId',columns='itemId',values='rating')
user_item_matrix = user_item_matrix.fillna(0)

sparse_matrix = csr_matrix(user_item_matrix.values)
train_data , test_data = train_test_split(user_item_matrix,test_size=0.2,random_state = 42)
train_sparse_matrix = csr_matrix(train_data)
test_sparse_matrix = csr_matrix(test_data)

#implementing collabrative filtering
n_components = 50
svd_model = TruncatedSVD(n_components=n_components,random_state=42)
svd_model.fit(train_sparse_matrix)

#step 5:make predictions
train_reduced = svd_model.transform(train_sparse_matrix)
test_reduced = svd_model.transform(test_sparse_matrix)


train_reconstructed = np.dot(train_reduced,svd_model.components_)
test_reconstructed = np.dot(test_reduced,svd_model.components_)


train_pred = pd.DataFrame(train_reconstructed,index = train_data.index,columns=train_data.columns)
test_pred = pd.DataFrame(test_reconstructed,index=test_data.index,columns=test_data.columns)

def calculate_rmse(true_matrix , predicted_matrix):
    true_values = true_matrix.values.flatten()
    predicted_values = predicted_matrix.values.flatten()
    mask = true_values!=0
    true_values = true_values[mask]
    predicted_values = predicted_values[mask]
    rmse =np.sqrt(mean_squared_error(true_values,predicted_values))
    return rmse
train_rmse = calculate_rmse(train_data,train_pred)
test_rmse = calculate_rmse(test_data,test_pred)
print(f"Train RMSE {train_rmse}")

print(f"test_rmse:{test_rmse}")

def recommend_items(user_id,num_recommendations=10):
    if(user_id not in test_pred.index):
        raise ValueError(f"Uer ID{user_id},not found in the test set")
    user_predictions = test_pred.loc[user_id]
    recommended_items = user_predictions.sort_values(ascending=False).head(num_recommendations)
    return recommended_items
valid_user_ids = test_pred.index.tolist()
user_id = valid_user_ids[0]
recommendations = recommend_items(user_id)

print(f"Top 10 recommendations for User {user_id}:\n{recommendations}")

