import sys
import pandas as pd
import pickle
from sklearn.metrics import fbeta_score, accuracy_score
import warnings
warnings.filterwarnings('ignore')


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv)) 

model = sys.argv[1]
X_test_path = sys.argv[2]
y_test_path = sys.argv[3]

# load the model from disk
loaded_model = pickle.load(open(model, 'rb'))
X_test = pd.read_csv(X_test_path)
y_test = pd.read_csv(y_test_path)

y_test_pred = loaded_model.predict(X_test)
acc_test = accuracy_score(y_test, y_test_pred)
f_test = fbeta_score(y_test, y_test_pred,beta=0.5)

print (f'Accuracy on testing data: {acc_test}')
print (f'F_beta_score on test data: {f_test}')

