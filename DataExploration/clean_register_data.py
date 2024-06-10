import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from helper import *

data = pd.read_csv("Data/esma_register.csv", encoding="utf-8")

# filter out columns that are all nans
pct_nans = data.isna().sum() / len(data)
nan_idx = pct_nans[pct_nans==1].index
data = data.drop(nan_idx, axis=1)

# rename columns to meaningful names
data = data.rename(columns=relevant_columns_rename_dict)
data = data[list(relevant_columns_rename_dict.values())]

# restrict data to interesting entity types only
data = data[(data["ENTITY_TYPE"].isin(entity_filter))&(data["STATUS"]=="Active")].reset_index(drop=True)
data["LOC"] = data["BRANCH_LOC"].fillna(data["HQ_LOC"])
data["COUNTRY"] = data["HOST_COUNTRY"].fillna(data["HOME_COUNTRY"])

nice_countries = ["FRANCE", "ITALY", "SPAIN", "GERMANY", "NETHERLANDS", "LUXEMBOURG", "PORTUGAL", "BELGIUM", "UNITED KINGDOM"]
data = data[data["COUNTRY"].isin(nice_countries)].copy()

df_locations = data[["NAME","ENTITY_TYPE", "LOC"]].dropna().copy()
df_locations.to_csv("Data/locations.csv")

pkl_dump(data, "data.pkl","Data/")






tmp = data.value_counts(["COMPETENT_AUTHORITY", "HOME_COUNTRY"]).reset_index()



data






data[data["HOST_COUNTRY"].notna()]["BRANCH_ADDRESS"].isna().sum()

data[data["HOST_COUNTRY"].notna()][["HQ_ADDRESS","BRANCH_ADDRESS"]].isna().sum()

data[data["HOST_COUNTRY"].isna()][["HQ_ADDRESS","BRANCH_ADDRESS"]].notna().sum()

data["LOCATION"] = data["BRANCH_ADDRESS"].fillna(data["HQ_ADDRESS"])


data[data["HQ_ADDRESS"]!=data["BRANCH_ADDRESS"]][["HQ_ADDRESS","BRANCH_ADDRESS"]]


data[["HQ_ADDRESS","BRANCH_ADDRESS"]].isna().sum()


data["collectorParent"].isna().sum()

for col in data.columns:
    print(data[col].value_counts().head(5))
    print()

tmp = data[data["NAME"].str.contains("APG")]

data
entity_filter


data.columns

data["ae_entityTypeLabel"].value_counts()

tmp = data[data["ae_homeMemberState"] == "NETHERLANDS"]

tmp["ae_entityTypeLabel"].value_counts()

import plotly.express as px




