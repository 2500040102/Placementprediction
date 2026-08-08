import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C:/Users/Dell/PycharmProjects/placement_prediction/dataset/placement_predict_50K_Raw.csv")
print ("---First 5 rows")
print(df.head())
print("---First 6 columns")
subset=df.iloc[:,0:6]
print(subset)
missing_counts=df.isnull().sum()
print("---Missing values per column----")
print(missing_counts)
print("-"*40)

duplicate_rows = df[df.duplicated()]
print(f"Total duplicate rows detected: {len(duplicate_rows)}")
print(duplicate_rows)
print("-"*40)
plt.figure(figsize=(20,10))
sns.heatmap(df.isnull(),cbar="False",cmap="virdis")
plt.title("Missing Values Heatmap")
plt.show()

