import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import SVC
from sklearn.metrics import fbeta_score, accuracy_score
from imblearn.over_sampling import RandomOverSampler
import pickle
from imblearn.over_sampling import RandomOverSampler
import warnings
warnings.filterwarnings('ignore')

from feature_engineering import drop_semer, use_non_use, make_int, drug_groups_join

#Import Data
df = pd.read_excel('Data/drug_consumption.xls')
print("Read in Data")

#Adjust dataset to business problem
df=drop_semer(df)
df=use_non_use(df)
df=make_int(df)
df=drug_groups_join(df)
print ("Adjusted dataset")

#Split Data into X and Y
X = df[['Age', 'Gender', 'Education', 'Country', 'Ethnicity', 'Nscore', 'Escore', 'Oscore', 'Ascore', 'Cscore', 'Impulsive', 'SS']]
y = df['Group2_drugs']
print("Saved X and y")

#Train-Test-Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0, stratify = y) 

print("Saving test data in the data folder")
X_test.to_csv("data_model/X_test.csv", index=False)
y_test.to_csv("data_model/y_test.csv", index=False)

# Define oversampling strategy
oversample = RandomOverSampler(sampling_strategy='minority')
X_train, y_train = oversample.fit_resample(X_train, y_train)

print ("Training set has {} samples.".format(X_train.shape[0]))
print ("Testing set has {} samples.".format(X_test.shape[0]))

# Training the model
clf = SVC(random_state = 420)
learner = clf.fit(X_train, y_train)

# Train set
predictions_train = learner.predict(X_train)
acc_train = accuracy_score(y_train, predictions_train)
f_train = fbeta_score(y_train,predictions_train,beta=0.5)

#Test set
predictions_test = learner.predict(X_test)
acc_test = accuracy_score(y_test, predictions_test)
f_test = fbeta_score(y_test,predictions_test,beta=0.5)

print (f'Accuracy on trainig data: {acc_train}')
print (f'Accuracy on testing data: {acc_test}')
print (f'F_beta_score on trainig data: {f_train}')
print (f'F_beta_score on test data: {f_test}')

#saving the model
print("Saving model in the model folder")
filename = 'models/SVC.sav'
pickle.dump(learner, open(filename, 'wb'))