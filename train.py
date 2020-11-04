import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVC
import pickle
from imblearn.over_sampling import RandomOverSampler
import warnings
warnings.filterwarnings('ignore')

from feature_engineering import drop_semer, use_non_use, drug_group_1, drug_group_2, drug_group_3, drug_groups_join

#Import Data
df = pd.read_excel('Data/drug_consumption.xls')

print("Read dataframe")