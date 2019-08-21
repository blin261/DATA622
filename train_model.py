import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split



def model(X, y):

	#Inpute the datasets for missing values and create a random forest classifier.
    imp = Imputer(missing_values = np.nan, strategy = 'mean')
    clf = RandomForestClassifier(n_estimators = 100, max_depth = 2, random_state = 0)
    steps = [("imputation", imp), ("random_forest", clf)]
    pipeline = Pipeline(steps)
    
	#Split the datasets for both training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state=42)
    
	#Save the test dataset 
    X_test.to_csv("X_test.csv")
    y_test.to_csv("y_test.csv")
    
	#Fit the model
    m = pipeline.fit(X_train, y_train)
    return m

def main():

	#Load the dataset using pandas as a dataframe
    df = pd.read_csv("https://raw.githubusercontent.com/cunyfalldata622s2/homework2-blin261/master/titanic_train.csv")
	
	#Drop any unnecessary variables
    df = df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = 1)
	
	#Convert some categorical variables (sex and embarked) to dummy variables or in other words binary variables
    df = pd.get_dummies(df)
	
	#Sex_female and Embarked_C contain same information as the other variables.
    new_df = df.drop(["Sex_female", "Embarked_C"], axis = 1)
    
	#Variable "Survived" is our dependent variable and all the others are our independent variables.
    y = new_df["Survived"]
    X = new_df.drop("Survived", axis = 1)
    m = model(X, y)
    
	#Save the output of Random Forest Model as pkl file.
    output = open('model.pkl', 'wb')
    pickle.dump(m, output)
    
    
if __name__=="__main__":
    main()