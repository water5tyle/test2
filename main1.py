import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
table = pd.read_csv("1.csv")
# print(table[0:20]["Unnamed: 0"])
table = table.drop(["Unnamed: 0", "Unnamed: 1"], axis='columns')
table = table.transpose()
table = table.drop([0, 1, 2, 3, 4], axis='columns')
table = table.reset_index()
# print(table.columns)
# table = table.drop([0], axis='rows')
table.index = table[5]
table.index.name = "user"
# print(table.index)
# print(table[5])
table = table.drop([5], axis='columns')
print(table.groupby(6)['user'].count)
# print(table[:]["Unnamed: 0"])
# print(table[table["Unnamed: 1"] == '✔'][:])
# print(table[:][0:100])
