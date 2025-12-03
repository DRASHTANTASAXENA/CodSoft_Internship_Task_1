from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
data['Sex'] = le_sex.fit_transform(data['Sex'])
data['Embarked'] = le_Embarked.fit_transform(data['Embarked'])
x_train, x_test, y_train, y_test = train_test_split(
model = LogisticRegression(max_iter=200)
model.fit(x_train, y_train)
rf_model.fit(x_train, y_train)