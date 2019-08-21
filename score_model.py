from sklearn.metrics import classification_report
import pandas as pd
import pickle

#Create a function to help clean up the data
def data_prep(df):
    df = df.drop(["PassengerId", "Name", "Ticket", "Cabin"], axis = 1)
    df = pd.get_dummies(df)
    new_df = df.drop(["Sex_female", "Embarked_C"], axis = 1)
    return new_df

	
def main():
	#Load all necessary CSV files
    X_test = pd.read_csv("X_test.csv")
    y_test = pd.read_csv("y_test.csv")
    titanic_test = pd.read_csv("titanic_test.csv")
    
	#Drop any unnecessary columns and rows
    X_test.drop(X_test.columns[[0]], axis = 1, inplace = True)
    y_test.drop(y_test.columns[[0]], axis = 1, inplace = True)
    X_test.drop(X_test.index[0], inplace = True)
    
	
	#Load the pickle file which store the random forest model that was created earlier
    p = open("model.pkl")
    rfc_model = pickle.load(p)
    
	#Calculate the accuracy score and create classification report
    score = rfc_model.score(X_test, y_test)
    y_pred = rfc_model.predict(X_test)
    report = classification_report(y_test, y_pred)
    
	
	#Make prediction for the test dataset
    input = data_prep(titanic_test)    
    test_pred = rfc_model.predict(input)
    
	
	#Output the results
    print("The model's accuracy score is", score)
    print("The Classification report is", report)
    print("The predicted value for the titanic test set is", test_pred)
    
    
if __name__ == "__main__":
    main()