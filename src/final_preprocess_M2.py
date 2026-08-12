import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler
input_file="C:/Users/Dell/PycharmProjects/placement_prediction/dataset/placement_predict_50K_Raw.csv"
output_file="C:/Users/Dell/PycharmProjects/placement_prediction/dataset/final_preprocess_M2.csv"
df=pd.read_csv(input_file)
processed_df=df.copy()
print("Original Dataset Shape:" , processed_df.shape)
processed_df.drop_duplicates(inplace=True)
numeric_cols= processed_df.select_dtypes(include=['int64','float']).columns
for col in numeric_cols:
    processed_df[col].fillna(processed_df[col].median(),inplace=True)
categorical_cols=processed_df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    processed_df[col].fillna(processed_df[col].median()[0],inplace=True)
for col in categorical_cols:
    processed_df[col] = processed_df[col].str.strip()
    processed_df[col]=processed_df[col].str.lower()
encoder=LabelEncoder()
for col in categorical_cols:
    processed_df[col]=encoder.fit_transform(processed_df[col])
scaler=StandardScaler()
processed_df[numeric_cols]=scaler.fit_transform(
    processed_df[numeric_cols]
)
processed_df.to_csv(output_file,index=False)
print("\nPreprocessing Completed Successfully!")
print("Original Dataset Shape :",df.shape)
print("Processed Dataset Shape :",processed_df.shape)
print("Saved File:" ,output_file)