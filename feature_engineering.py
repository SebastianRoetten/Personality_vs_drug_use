import pandas as pd
import numpy as np


def drop_semer(df:pd.DataFrame)-> pd.DataFrame:
    df = df.drop(df.loc[df["Semer"] != "CL0"].index)
    df.drop('Semer', inplace=True, axis=1)
    return df 



def use_non_use(df:pd.DataFrame)-> pd.DataFrame:
    drugs = ["Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack",
        "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA"]

    for element in drugs:
        column_insert = df.columns.get_loc(element)+1
        col_name = element+"_Cat"
        cat = df[element].apply(lambda x: 0 if (x == "CL0" or x == "CL1") else 1)
        df.insert(column_insert, col_name, cat)
        df[col_name] = df[col_name].astype("category")
    
    return df

def make_int(df):
    df["Alcohol_Cat"] = df["Alcohol_Cat"].astype(int)
    df["Caff_Cat"] = df["Caff_Cat"].astype(int)
    df["Cannabis_Cat"] = df["Cannabis_Cat"].astype(int)
    df["Choc_Cat"] = df["Choc_Cat"].astype(int)
    df["Nicotine_Cat"] = df["Nicotine_Cat"].astype(int)

    df["Amphet_Cat"] = df["Amphet_Cat"].astype(int)
    df["Benzos_Cat"] = df["Benzos_Cat"].astype(int)
    df["Coke_Cat"] = df["Coke_Cat"].astype(int)
    df["Ecstasy_Cat"] = df["Ecstasy_Cat"].astype(int)
    df["Legalh_Cat"] = df["Legalh_Cat"].astype(int)
    df["LSD_Cat"] = df["LSD_Cat"].astype(int)
    df["Shrooms_Cat"] = df["Shrooms_Cat"].astype(int) 

    df["Amyl_Cat"] = df["Amyl_Cat"].astype(int)   
    df["Crack_Cat"] = df["Crack_Cat"].astype(int)
    df["Heroin_Cat"] = df["Heroin_Cat"].astype(int)
    df["Ketamine_Cat"] = df["Ketamine_Cat"].astype(int)
    df["Meth_Cat"] = df["Meth_Cat"].astype(int)
    df["VSA_Cat"] = df["VSA_Cat"].astype(int)

    return df


def drug_groups_join(df):
    df['Group1_drugs']= df["Alcohol_Cat"] + df["Caff_Cat"] + df["Cannabis_Cat"] + df["Choc_Cat"] + df["Nicotine_Cat"]
    df['Group1_drugs'] = df['Group1_drugs'].apply(lambda x: 1 if x > 0 else 0)

    df['Group2_drugs']= df["Amphet_Cat"] + df["Benzos_Cat"] + df["Coke_Cat"] + df["Ecstasy_Cat"] + df["Legalh_Cat"] + df["LSD_Cat"]+ df["Shrooms_Cat"]
    df['Group2_drugs'] = df['Group2_drugs'].apply(lambda x: 1 if x > 0 else 0)

    df['Group3_drugs']= df["Amyl_Cat"] + df["Crack_Cat"] + df["Heroin_Cat"] + df["Ketamine_Cat"] + df["Meth_Cat"] + df["VSA_Cat"]
    df['Group3_drugs'] = df['Group3_drugs'].apply(lambda x: 1 if x > 0 else 0)  

    df.drop(["Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack","Ecstasy", "Heroin", "Ketamine",
          "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA", "Alcohol_Cat", "Amphet_Cat", "Amyl_Cat", "Benzos_Cat", "Caff_Cat",
          "Cannabis_Cat", "Choc_Cat", "Coke_Cat", "Crack_Cat","Ecstasy_Cat", "Heroin_Cat", "Ketamine_Cat", "Legalh_Cat", "LSD_Cat", 
          "Meth_Cat", "Shrooms_Cat", "Nicotine_Cat", "VSA_Cat"], axis=1, inplace=True)
    
    return df