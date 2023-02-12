import requests
from bs4 import BeautifulSoup

result = requests.get("http://10.20.108.131:8080/opac/openlink.php?strSearchType=title&match_flag=forward&historyCount=1&strText=哈哈&doctype=ALL&with_ebook=on&displaypg=20&showmode=list&sort=CATA_DATE&orderby=desc&dept=ALL")
soup = BeautifulSoup(result.text, "html.parser")
list = soup.select('.book_list_info')
if len(list) == 0:
    print("没有找到相关书籍")
book = ""
for i in range(10):
    name = soup.select('.book_list_info h3 a')[i].text
    
    number = soup.select('.book_list_info p span')[i].text.replace(" ", "").replace("\t", "").replace("(0)馆藏", "")
    author = soup.select('.book_list_info p')[i].text.replace(" ", "").replace("\t", "").replace(number, "").replace("(0)馆藏", "")
    link = soup.select('.book_list_info h3 a')[i]['href'][17:65]
    book += name + "\n" + author + number + "\n\n" + link + "\n\n"
print(
    "好的，找到了这些：\n\n" + book + "重新查询？ 试试 /retry"
)
