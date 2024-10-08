import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {
    'page':['home','about','contact','services','blog'],
    'bounce_rate':[0.2,0.4,0.3,0.5,0.1],
    'avg_time_on_page':[120,80,60,100,200],
    'click_through_rate':[0.3,0.25,0.35,0.15,0.4],
    'scroll_depth':[0.8,0.6,0.7,0.5,0.9]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
sns.barplot(x='page',y='bounce_rate',data = df,width = 0.4,color="skyblue")
plt.xlabel('Page')
plt.ylabel('Bounce_Rate')
plt.title('Bounce Rate by Page')
plt.show()
plt.figure(figsize=(10,6))
sns.barplot(x='page',y='avg_time_on_page',data=df,width = 0.4,color = 'red')
plt.title("avg_time_on_page")
plt.show()
plt.figure(figsize=(10,6))
sns.barplot(x="page",y="click_through_rate",data = df,width=0.4,color="limegreen")
plt.title("click_through_rate")
plt.show()