# importing required libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

train_data = pd.read_csv('Dataset/train-data.csv')
test_data = pd.read_csv('Dataset/test-data.csv')

train_x = train_data.drop(columns=['Survived'], axis=1)
train_y = train_data['Survived']

test_x = test_data.drop(columns=['Survived'], axis=1)
test_y = test_data['Survived']

model_dict = {"Logistic Regression": LogisticRegression(),
              "Random Forest": RandomForestClassifier(),
              "Decision Tree": DecisionTreeClassifier()}
res_dict = {}

for name, models in model_dict.items():
    model = models

    model.fit(train_x, train_y)

    predict_train = model.predict(train_x)

    print('*' * 40)
    print(f'Model Name : {name}')
    print('*' * 40)

    # Accuray Score on train dataset
    accuracy_train = accuracy_score(train_y, predict_train)
    print('accuracy_score on train dataset : ', accuracy_train)

    predict_test = model.predict(test_x)

    # Accuracy Score on test dataset
    accuracy_test = accuracy_score(test_y, predict_test)
    print(f'accuracy_score on test dataset :{accuracy_test} \n\n')

    res_dict.update({name: accuracy_test})

max = 0
for name, score in res_dict.items():
    if score > max:
        max = score
        id = name

print(f'Best Model is :{id} with score {max}:')
