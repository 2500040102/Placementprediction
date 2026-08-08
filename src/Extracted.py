import pandas as pd

# Read the CSV file
df = pd.read_csv(r"C:\Users\Dell\Downloads\archive (1)\US_Accidents_March23.csv")

# Keep only the first 60,000 rows
df = df.head(60000)

# Save the new CSV
df.to_csv(r"C:\Users\Dell\Downloads\US_Accidents_60000.csv", index=False)

print("Done!")
print("Rows:", len(df))