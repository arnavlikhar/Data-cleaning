import csv
import pandas as pd

df=pd.read_csv("total_stars.csv")



del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]

df.to_csv('finalstars.csv') 