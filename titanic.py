import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
titanic_df = pd.read_csv('titanic.csv')
# print(titanic_df.info())
# print(titanic_df.groupby(['Sex', 'Survived', 'PClass'])['PassengerID'].count())
# print(titanic_df.groupby(["PClass", 'Age'])['PassengerID'].count())
# print(titanic_df.groupby(["Sex", 'Survived'])['Age'].mean())
# pvr = titanic_df.pivot_table(index='PClass', columns='Sex', aggfunc='count', values='PassengerID')
# print(pvr)
# print(titanic_df.head())

# print(titanic_df[:]["Sex"])
print(titanic_df.pivot(index="PassengerID", columns="Age", values="Age"))
