import pandas as pd
from bs4 import BeautifulSoup
import requests

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
    # list_students3 = get_students('biso03.xlsx')
    # list_students4 = get_students('biso04.xlsx')
    # list_students = list_students3 + list_students4
    # print(list_students)

    url=r"https://generatefakename.com/ru/address/ru/ru"
    url=r"https://www.mirea.ru/"
    page = requests.get(url)
    soup = BeautifulSoup(page, "html.parser")
    colleges = soup.findAll('h3')
    print(colleges)
if __name__ == '__main__':
    main()
