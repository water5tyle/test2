import pandas as pd
import itertools as it

df = pd.read_csv("1.csv")
region_ranges = {'Київська': [[1, 150]], 'Дніпровска': [[151, 190], [411, 449], [544, 551], [555, 558], [563, 572]],
                 'Вінницька': [[191, 300], [401, 410]], 'Львівська': [[301, 400]],
                 'Одеська': [[450, 543], [552, 554], [559, 562]]}
r = [261, 264]
# print(df.iloc[index])
counter = 0
var_counter = 1
print(f"Загально:")

for i in range(r[0], r[1]):
    for f, item in enumerate(df.iloc[i]):
        if '✔' in str(item) or 'nan' not in str(item):
            counter += 1
    # print(counter)
    print(f"{var_counter} - Кількість {counter} - Відсоток: {round((counter / 572) * 100, 1)}%")
    var_counter += 1
    counter = 0

text = ""
counter = 0
for region in region_ranges:
    all_ranges = []
    var_counter = 1
    text += f"{region}:\n"
    for ran in region_ranges[region]:
        all_ranges += range(ran[0], ran[1] + 1)
    print(all_ranges)
    for i in range(r[0], r[1]):
        for f, item in enumerate(all_ranges):
            # print(f, df.iloc[i][item+1])
            if '✔' in str(df.iloc[i][item+1]) or 'nan' not in str(df.iloc[i][item+1]):
                counter += 1
        text += f"{var_counter} - Кількість:{counter} - Відсоток: {round((counter / len(all_ranges)) * 100, 1)}%\n"
        counter = 0
        var_counter += 1
    print(text)
    text = ""