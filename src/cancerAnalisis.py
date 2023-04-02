from sklearn.preprocessing import StandardScaler
import pandas as pd
import json 
import math
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

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

# normalize the data
scaler = StandardScaler()
df = pd.DataFrame(data[['grade', 'tumorSize', 'age']])
df.dropna()
df = scaler.fit_transform(df)
resultArray = []


#loop to get the data of the 7690 rows
for ind in range(data.shape[0]):
    toAppend = 0
    if (data['cancerType'][ind] == cancerType):
        toAppend += 1 / (math.pow(df[ind][0] - grade, 2)+1)
        toAppend += 1 / (math.pow(df[ind][1] - tumorSize, 2)+1)
        if(data['ethnicity'][ind] == ethnicity):
            toAppend += 1
        toAppend += 1 / (math.pow(df[ind][2] - age, 2)+1)
        if(data['sex'][ind] == sex):
            toAppend += 1
        if(data["maritalStatus"][ind] == maritalStatus):
            toAppend += 1
        resultArray.append(toAppend)

#select index of ten greatest values in result array
resultArray = sorted(range(len(resultArray)), key=lambda i: resultArray[i])[-10:]



print()
print(df)
grades = data['grade'].values
tumor_sizes = data['tumorSize'].values
ages = data['age'].values
# print(grades)
X = np.column_stack((tumor_sizes, ages))
pca = PCA(n_components=2)
pca.fit(X)
X_pca = pca.transform(X)

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.show()
#select the ten greatest values in data
data = data['age'].iloc[resultArray]
f.close()