import pandas as pd
import numpy as np
pd.set_option("display.max_rows", None)
df = pd.read_csv("C:\\Users\\busra\\OneDrive\\Masaüstü\\persona.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())
print(df["SOURCE"].nunique())
print(df["SOURCE"].value_counts())
print(df["PRICE"].unique())
print(df["PRICE"].value_counts())
print(df["COUNTRY"].value_counts())
print(df.groupby("COUNTRY")["PRICE"].count())
print(df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count"))

print(df.groupby("COUNTRY")["PRICE"].sum())
print(df.groupby("COUNTRY").agg({"PRICE": "sum"}))
print(df.groupby("SOURCE")["PRICE"].sum())
print(df["SOURCE"].value_counts())

print(df.groupby("COUNTRY").agg({"PRICE": "mean"}))
print(df.groupby("SOURCE").agg({"PRICE": "mean"}))


print(df.groupby(["COUNTRY", "SOURCE","SEX","AGE"]).agg({"PRICE": "mean"}).head())

agg_df = df.groupby(by=["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
print(agg_df.head())


agg_df = agg_df.reset_index()
print(agg_df.head())



bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]


mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]


agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
print(agg_df.head())

agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cat']].agg(lambda x: '_'.join(x).upper(), axis=1)
print(agg_df.head())


agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})
print(agg_df.head())

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
print(agg_df)

# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente ve ortalama ne kadar gelir kazandırması beklenir?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
print(agg_df)

output_file = "output.xlsx"
agg_df.to_excel(output_file, index=False)







