import pandas as pd
df=pd.read_excel("1.xlsx")
# item=df.loc([1][1])
# print(df.head())
count_rows = df.shape[0]
print(count_rows)
list_students = []
for i in range(1, count_rows):
    item = str(df.loc[i][1])
    if len(item) > 3:
        list_students.append(item)

print(list_students)