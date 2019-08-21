import requests
import getpass 


#Get user's log in information
username = getpass.getpass("Username is")
password = getpass.getpass("Password is")
    
	
#Create payload to access kaggle datasets	
payload = {
    '__RequestVerificationToken': '',
    'username': username,
    'password': password,
    'rememberme': 'false'
}

#Kaggle's URL for login and download the data
login_url = 'https://www.kaggle.com/account/login'
train_url = "https://www.kaggle.com/c/titanic/download/train.csv"
test_url = "https://www.kaggle.com/c/titanic/download/test.csv"
    
	
#The filename that I want to use to save the data	
train_filename = "titanic_train.csv"
test_filename = "titanic_test.csv"
    
	
#Obtained AFToken Credentials. Code reference: https://stackoverflow.com/questions/50863516/issue-in-extracting-titanic-training-data-from-kaggle-using-jupyter-notebook/50876207#50876207
with requests.Session() as c:
    response = c.get(login_url).text
    AFToken = response[response.index('antiForgeryToken')+19:response.index('isAnonymous: ')-12]
    print("AntiForgeryToken={}".format(AFToken))
    payload['__RequestVerificationToken'] = AFToken
    c.post(login_url + "?isModal=true&returnUrl=/", data = payload)
	
r = c.get(train_url)
print(r)
f = open(train_filename, 'wb')
f.write(r.content)
f.close()
	
r = c.get(test_url)
print(r)
f = open(test_filename, 'wb')
f.write(r.content)
f.close()       