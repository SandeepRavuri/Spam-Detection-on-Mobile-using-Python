# importing Modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read csv file
data=pd.read_csv("E:\DATASCIENCE\project\Review\Documentation\spam.csv",encoding="latin_1")
print(data.head())

#find no.of rows and columns
print(data.shape)

#find if any NaN numbers is there in data
print(data.isnull().sum())

#Drop NAN Number columns
data = data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)

#column names rechange
data = data.rename(columns={"v1":"label", "v2":"text"})

#Count observations in each label
print(data.label.value_counts())

# convert label to a numerical variable
data['label_num'] = data.label.map({'ham':0, 'spam':1})
data['length'] = data['text'].apply(len)
print(data.head())

# importing the seaborn for ploting the graph
import seaborn as sns
sns.countplot(data["label"])
print(plt.show())
data["label"].value_counts().plot(kind="pie",autopct="%1.1f%%")
plt.axis("equal")
print(plt.show())

#checking how many spam mails are there
spam1=data.loc[data['label']=='spam']
print(spam1["text"].head())

#checking how many ham mails are there
ham1=data.loc[data['label']=='ham']
print(ham1["text"].head())

# Assume x value as a input 
x=np.array(data.iloc[0:500,1])
print(x[0:5])
print(x.shape)

# assume y value as target value
y=np.array(data.iloc[0:500,0])
print(y[0:5])
print(y.shape)

#importing the Sklearn module
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

# importing the CountVector from Feature extraction
from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()
print(count_vector)

#apply count vector to convert text data vector format like 0s and 1s
train_data = count_vector.fit_transform(x_train)
test_data = count_vector.transform(x_test)

# importing the naive bayes algorithm form sklearn
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(train_data,y_train)

#find the prediction 
pred=model.predict(test_data)
print(pred)

#checking accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(pred,y_test)
print(score)

# Testing
from sklearn.metrics import classification_report
nbreport=classification_report(y_test, pred)
print(nbreport)

from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score

y=[f1_score(y_test,pred),recall_score(y_test,pred),precision_score(y_test,pred)]
x=["f1score","recall","precision"]
y=[f1_score(y_test,pred),recall_score(y_test,pred),precision_score(y_test,pred)]
df = pd.DataFrame(dict(x=x, y=y))
df

sns.factorplot("x","y", data=df,kind="bar")
plt.show()

sns.barplot("x","y", data=df)
plt.show()

plt.pie(y,labels=x,autopct='%1.1f%%')
plt.axis("equal")
plt.show()

#creating testing data
x_test=[ "hi how are you",
        "Free entry in 2 a wkly comp to win FA Cup fina...",
        "when will you go to home",
        "i will call you back",
        "are you busy now"]

x_test.append("goodmoring")
x_test.append("WINNER!! As a valued network customer you have...")
x_test

x_test1=np.array(x_test)
x_test1

X_train=data.iloc[0:200,1]
X_train[0:6]

Y_train=data.iloc[0:200,0]
Y_train[0:5]

from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()
print(count_vector)

train_data = count_vector.fit_transform(X_train)
test_data = count_vector.transform(x_test1)

train_data.shape
test_data.shape

Y_train.shape
from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(train_data,Y_train)
pred=model.predict(test_data)
pred
y1=model.predict(test_data)
y1
df = pd.DataFrame(dict(INPUT=x_test1, OUTPUT=y1))
df
df.iloc[4:]
