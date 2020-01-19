import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import time

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

name: str

for name, models in model_dict.items():
    def timeit(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            res = str((end - start) * 1000)
            res_dict.update({name: res})
            print('-'*40)
            print(name + " took " + res + " mSec")
            print('-'*40)
            return result

        return wrapper


    @timeit
    def function():
        model = models

        model.fit(train_x, train_y)

        predict_train = model.predict(train_x)

        # Accuray Score on train dataset
        accuracy_train = accuracy_score(train_y, predict_train)

        predict_test = model.predict(test_x)

        # Accuracy Score on test dataset
        accuracy_test = accuracy_score(test_y, predict_test)
    function()

best = min(res_dict.values())
result = [key for key in res_dict if res_dict[key] == best]
print('*' * 40)
print(f'Best Model in performance is: {result} with time {best}:')
print('*' * 40)
