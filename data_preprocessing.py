data['Age'].fillna(data['Age'].mean(), inplace=True)
data.drop(['Cabin'], axis=1, inplace=True)
data['Embarked'].fillna("S", inplace=True)
x = data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]