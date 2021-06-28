import pandas as pd
import numpy as np
df=pd.read_csv("train.csv")
lack=df.isnull()
#print(lack)
lack_col=lack.any()
#print(lack_col)
df_lack_only=df[df.isnull().values == True]
#print(df_lack_only)
df_del_lack_row = df.dropna(axis=0)
df_fill_lack2 = df.fillna(df.mean())
df = df_fill_lack2.drop_duplicates()
print(df)
