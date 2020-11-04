import pandas as pd
import numpy as np


def drop_semer(df:pd.DataFrame)-> pd.DataFrame:
    df = df.drop(df.loc[df["Semer"] != "CL0"].index)
    df.drop('Semer', inplace=True, axis=1)



def use_non_use(df:pd.DataFrame)-> pd.DataFrame:
    drugs = ["Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack",
        "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA"]

    for element in drugs:
        column_insert = df.columns.get_loc(element)+1
        col_name = element+"_Cat"
        cat = df[element].apply(lambda x: 0 if (x == "CL0" or x == "CL1") else 1)
        df.insert(column_insert, col_name, cat)
        df[col_name] = df[col_name].astype("category")



def drug_group_1(df:pd.DataFrame)-> pd.DataFrame:
    df_group1_drugs = df.drop(["Amphet_Cat", "Amyl_Cat", "Benzos_Cat", "Coke_Cat", "Crack_Cat", "Ecstasy_Cat", 'Heroin_Cat', 'Ketamine_Cat', 
                        'Legalh_Cat', 'LSD_Cat', 'Meth_Cat', 'Shrooms_Cat', 'VSA_Cat', 'Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 
                        'Cannabis', 'Choc', 'Coke', 'Crack', 'Ecstasy', 'Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth', 'Shrooms',
                        'Nicotine', 'VSA'], axis=1)

    df_group1_drugs["Alcohol_Cat"] = df_group1_drugs["Alcohol_Cat"].astype(int)
    df_group1_drugs["Caff_Cat"] = df_group1_drugs["Caff_Cat"].astype(int)
    df_group1_drugs["Cannabis_Cat"] = df_group1_drugs["Cannabis_Cat"].astype(int)
    df_group1_drugs["Choc_Cat"] = df_group1_drugs["Choc_Cat"].astype(int)
    df_group1_drugs["Nicotine_Cat"] = df_group1_drugs["Nicotine_Cat"].astype(int)



def drug_group_2(df:pd.DataFrame)-> pd.DataFrame:
    df_group2_drugs = df.drop(["Alcohol_Cat", "Amyl_Cat", "Caff_Cat", "Cannabis_Cat", "Choc_Cat", "Crack_Cat",
                        "Heroin_Cat", "Ketamine_Cat", "Meth_Cat", "Nicotine_Cat", "VSA_Cat", "Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack",
                        "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA"], axis=1)
    
    df_group2_drugs["Amphet_Cat"] = df_group2_drugs["Amphet_Cat"].astype(int)
    df_group2_drugs["Benzos_Cat"] = df_group2_drugs["Benzos_Cat"].astype(int)
    df_group2_drugs["Coke_Cat"] = df_group2_drugs["Coke_Cat"].astype(int)
    df_group2_drugs["Ecstasy_Cat"] = df_group2_drugs["Ecstasy_Cat"].astype(int)
    df_group2_drugs["Legalh_Cat"] = df_group2_drugs["Legalh_Cat"].astype(int)
    df_group2_drugs["LSD_Cat"] = df_group2_drugs["LSD_Cat"].astype(int)
    df_group2_drugs["Shrooms_Cat"] = df_group2_drugs["Shrooms_Cat"].astype(int)   



def drug_group_3(df:pd.DataFrame)-> pd.DataFrame:
    df_group3_drugs = df.drop(["Alcohol_Cat", "Amphet_Cat", "Benzos_Cat", "Caff_Cat", "Cannabis_Cat", "Choc_Cat", "Coke_Cat",
                        "Ecstasy_Cat", "Legalh_Cat", "LSD_Cat", "Shrooms_Cat", "Nicotine_Cat", "Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack",
                        "Ecstasy", "Heroin", "Ketamine", "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA"], axis=1)  

    df_group3_drugs["Amyl_Cat"] = df_group3_drugs["Amyl_Cat"].astype(int)
    df_group3_drugs["Crack_Cat"] = df_group3_drugs["Crack_Cat"].astype(int)
    df_group3_drugs["Heroin_Cat"] = df_group3_drugs["Heroin_Cat"].astype(int)
    df_group3_drugs["Ketamine_Cat"] = df_group3_drugs["Ketamine_Cat"].astype(int)
    df_group3_drugs["Meth_Cat"] = df_group3_drugs["Meth_Cat"].astype(int)
    df_group3_drugs["VSA_Cat"] = df_group3_drugs["VSA_Cat"].astype(int)



def drug_groups_join(df:pd.DataFrame)-> pd.DataFrame:
    df['Group1_drugs']= df_group1_drugs["Alcohol_Cat"] + df_group1_drugs["Caff_Cat"] + df_group1_drugs["Cannabis_Cat"] + df_group1_drugs["Choc_Cat"] + df_group1_drugs["Nicotine_Cat"]
    df['Group1_drugs'] = df['Group1_drugs'].apply(lambda x: 1 if x > 0 else 0)

    df['Group2_drugs']= df_group2_drugs["Amphet_Cat"] + df_group2_drugs["Benzos_Cat"] + df_group2_drugs["Coke_Cat"] + df_group2_drugs["Ecstasy_Cat"] + df_group2_drugs["Legalh_Cat"] + df_group2_drugs["LSD_Cat"]+ df_group2_drugs["Shrooms_Cat"]
    df['Group2_drugs'] = df['Group2_drugs'].apply(lambda x: 1 if x > 0 else 0)

    df['Group3_drugs']= df_group3_drugs["Amyl_Cat"] + df_group3_drugs["Crack_Cat"] + df_group3_drugs["Heroin_Cat"] + df_group3_drugs["Ketamine_Cat"] + df_group3_drugs["Meth_Cat"] + df_group3_drugs["VSA_Cat"]
    df['Group3_drugs'] = df['Group3_drugs'].apply(lambda x: 1 if x > 0 else 0)  

    df.drop(["Alcohol", "Amphet", "Amyl", "Benzos", "Caff", "Cannabis", "Choc", "Coke", "Crack","Ecstasy", "Heroin", "Ketamine",
          "Legalh", "LSD", "Meth", "Shrooms", "Nicotine", "VSA", "Alcohol_Cat", "Amphet_Cat", "Amyl_Cat", "Benzos_Cat", "Caff_Cat",
          "Cannabis_Cat", "Choc_Cat", "Coke_Cat", "Crack_Cat","Ecstasy_Cat", "Heroin_Cat", "Ketamine_Cat", "Legalh_Cat", "LSD_Cat", 
          "Meth_Cat", "Shrooms_Cat", "Nicotine_Cat", "VSA_Cat"], axis=1, inplace=True)