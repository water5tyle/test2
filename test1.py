import pandas as pd

users = [{'user': 'loh', 'date': '2021-01', 'costs': 20}, {'user': 'loh', 'date': '2021-02', 'costs': 25}]
users.append({'user': 'loh1', 'date': '2021-02', 'costs': 130})
users.append({'user': 'loh1', 'date': '2021-03', 'costs': 250})
df_users = pd.DataFrame(users)

pv = df_users.pivot(index="user", columns="date", values="costs")
print(pv)
