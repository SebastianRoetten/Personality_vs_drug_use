# Personality_vs_drug_use
Personality vs. Risk of Drug USe


## Environment
```bash
conda env create -n drugs -f environment.yml  
conda install -c anaconda xlrd  
```


## Stakeholder:
The stakeholder is an international drug dealer who sells his drugs, mainly party drugs, on the dark web.  
Before individuals can enter the webpage and explore the different product, they have to fill in a personality questionaire, on which certain personality scores can be based. The drug dealer wants a model to predict whether a person is likely to consume party drugs based on these scores as well as some personal information. Individuals who would not purchase anything will not be allowed to enter the website, as he wants to stop people, who aren't actually interested in purchasing drugs, to see the website and then report him.


## What files to look at
Final_EDA.ipynb - Complete and final EDA 
SVC.ipynb - Final model with error anaylsis and zooming in on errors
data_cleaning.ipynb - Data cleaning process
model_comparison.ipynb - Model testing


## Using the Model
In order to train the model and store test data in the data folder and the model in models run:

```bash
python train.py  
```

In order to test that predict works on a test set you created run:

```bash
 python predict.py models/SVC.sav data_model/X_test.csv data_model/y_test.csv
```
