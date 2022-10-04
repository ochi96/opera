# # import spleeter as sp
import os
import pandas as pd
path = "E:\Projects\Freelancing\Opera audio files"

df = pd.read_csv(path + "\data_with_subregisters.csv")
print(df.head())
# print(os.listdir("E:\Projects\Freelancing\Opera audio files"))

for subregister in df.subregister.unique():
    selected_subregister = df.loc[lambda df: df.subregister == subregister, : ]
    selected_subregister.to_csv(path + "\{}.csv".format(subregister))

print(df.subregister.unique())


