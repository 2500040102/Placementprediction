import pandas as pd
input_file="C:/Users/Dell/PycharmProjects/placement_prediction/dataset//placement_predict_50K_Raw.csv"
output_file="C:/Users/Dell/PycharmProjects/placement_prediction/dataset/clean_del_mean_model_M2.csv"
df=pd.read_csv(input_file)
print("=" *70)
print("ORIGINAL PLACEMENT PREDICTION DATASET")