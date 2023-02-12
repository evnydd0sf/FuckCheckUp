import requests
from bs4 import  BeautifulSoup
from openpyxl import load_workbook, Workbook


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4051.0 Safari/537.36 Edg/82.0.425.0'}

excel = Workbook()
fileSheet = excel.active

with open("nua.txt", "r") as f:
    for line in f.readlines():
        try:
            line = line.strip('\n')
            url = 'http://' + line
            r = requests.get(url, headers=headers)
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'lxml')
            fileSheet.append([url, r.status_code, soup.title.text])
            excel.save('data.xlsx')
            print(url, r.status_code, soup.title.text)
        except Exception as e:
            fileSheet.append([url, r.status_code, 'error'])
            excel.save('data.xlsx')
            print('error')

