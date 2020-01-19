import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus

iris = load_iris()

df= pd.DataFrame(iris.data, columns= iris.feature_names)
df['target'] = iris.target
df['flower_name'] = df['target'].apply(lambda x: iris.target_names[x])
x = df.drop(['target','flower_name'], axis='columns')
y=df['target']
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2)

model = DecisionTreeClassifier(criterion='entropy')

model.fit(x_train, y_train)

score=model.score(x_test, y_test)

dot_data = StringIO()
export_graphviz(model, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

# Create PDF
graph.write_pdf("iris.pdf")

# Create PNG
graph.write_png("iris.png")

# this will create  decision tree plot, pdf and png file in the  working directory location..............