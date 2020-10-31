# Personality_vs_drug_use
Personality vs. Risk of Drug USe

## Environment 
conda create --name drugs python=3.8.5  
conda install -n drugs ipython  
conda install -n drugs jupyterlab  
conda install -n drugs seaborn  
conda install -n drugs sklearn  
conda install -c anaconda statsmodels  
conda install -n drugs scikit-learn  
conda install -n drugs pytest==6.1.1  
conda install -c anaconda xlrd  


## What to do/what to predict:
The stakeholder is a drugdealer who would like to predict what drugs they could sell to an individual. 
1. Categorize the drugs: e.g. party drugs, Psychedelics etc.
2. Change the different catgories of drug usage to no (never or a decade ago) or yes (everything else)
3. Predict what drug, if any, an individual would take 

**Things to look into:**
* Compare drug usage in the US and UK (other countries have too little data points)
* See if certain ethnicity lean towards certain drugs (very unbalanced data)
* See if education level has an impact on drug usage (also very unbalanced data)
* Look at different personality traits, e.g. individuals who are sensation seekers preder uppers or party drugs etc.