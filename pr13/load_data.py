import pandas as pd


def get_students(fileName):
    df = pd.read_excel(fileName)
    # print(df.head())
    # print(df.loc[4][1])
    count_rows = df.shape[0]
    list_students = []
    for i in range(1, count_rows):
        item = str(df.loc[i][1])
        if len(item) > 3:
            list_students.append(item)
    return list_students


def main():
    list_students3 = get_students('biso03.xlsx')
    list_students4 = get_students('biso04.xlsx')
    list_students = list_students3 + list_students4
    print(list_students)


if __name__ == '__main__':
    main()
