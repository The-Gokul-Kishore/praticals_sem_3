import pandas as pd
import numpy as np
def candidate_elimination(concepts,target):
    specific_h = concepts[0].copy()
    general_h = [['?' for _ in range(len(specific_h))] for i in range(1)]

    print("Intial specifc hypothesis(s):",specific_h)
    print("Intial general hypothesis(g):",general_h)

    for i ,instance in enumerate(concepts):
        if(target[i]=='yes'):
            print(f"\n instance {i+1} is a positive instance example: {instance}")
            for x in range(len(specific_h)):
                if(instance[x]!=specific_h[x]):
                    specific_h[x] = '?'
            print(f"updated specific hypothesis (s):{specific_h}")
        if(target[i]=='no'):
            print(f"\n instance {i+1} is a negative instance example: { instance}")
            for g in general_h.copy():
                for x in range(len(g)):
                    if g[x]!='?'and instance[x]!=g[x]:
                        general_h.append([specific_h[y] if y==x else '?' for y in range(len(specific_h))])
                general_h.remove(g)
                print(f"updated general hypotheisis(G):{general_h}")
        
    final_general_h = [h for h in general_h if any(attr!='?' for attr in h)]
    return specific_h,final_general_h

# Define columns for the dataset
columns = ['Sky', 'AirTemp', 'Humidity', 'Wind', 'Water', 'Forecast', 'EnjoySport']

# Define possible values for each column to generate synthetic data
data = pd.DataFrame({
        'Sky': ['Sunny', 'Sunny', 'Rainy', 'Sunny', 'Rainy', 'Sunny'],
        'AirTemp': ['Warm', 'Warm', 'Cold', 'Warm', 'Cold', 'Warm'],
        'Humidity': ['Normal', 'High', 'High', 'High', 'High', 'Normal'],
        'Wind': ['Strong', 'Strong', 'Strong', 'Strong', 'Strong', 'Weak'],
        'Water': ['Warm', 'Warm', 'Warm', 'Cool', 'Cool', 'Warm'],
        'Forecast': ['Same', 'Same', 'Change', 'Change', 'Change', 'Same'],
        'EnjoySport': ['yes', 'yes', 'no', 'yes', 'no', 'yes']
    })

    # Separate concepts (X) and target labels (Y)
concepts = np.array(data.iloc[:, :-1])
target = np.array(data.iloc[:, -1])

specific_h, general_h = candidate_elimination(concepts, target)

    # Print the final hypotheses
print("\nFinal Specific Hypothesis (S):", specific_h)
print("Final General Hypothesis (G):", general_h)