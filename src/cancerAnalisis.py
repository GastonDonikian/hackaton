
import pandas as pd
import json 
import math

#get data from userInput json
f = open('./userInput.json')
user = json.load(f)


cancerType = user.get('cancerType')
grade = user.get('grade')
tumorSize = user.get('tumorSize')
ethnicity = user.get('ethnicity')
age = user.get('age')
sex = user.get('sex')
maritalStatus = user.get('maritalStatus')

#import data form the dataUs.csv file
data = pd.read_csv('./dataUs.csv')
print(data.shape)
#show the type of the data columns
print(data.dtypes)
print(data.shape[0])
resultArray = []
#loop to get the data of the 7690 rows
print(data.shape)
for ind in range(data.shape[0]):
    toAppend = 0
    if (data['cancerType'][ind] == cancerType):
        print(data['grade'][ind])
        print(ind)
        toAppend += 1 / (math.pow(data['grade'][ind] - grade, 2)+1)
        toAppend += 1 / (math.pow(data['tumorSize'][ind] - tumorSize, 2)+1)
        if(data['ethnicity'][ind] == ethnicity):
            toAppend += 1
        toAppend += 1 / (math.pow(data['age'][ind] - age, 2)+1)
        if(data['sex'][ind] == sex):
            toAppend += 1
        if(data["maritalStatus"][ind] == maritalStatus):
            toAppend += 1
        resultArray.append(toAppend)
print(resultArray)
#select index of ten greatest values in result array
resultArray = sorted(range(len(resultArray)), key=lambda i: resultArray[i])[-10:]
print(resultArray)
#select the ten greatest values in data
data = data['age'].iloc[resultArray]
print(data)
f.close()