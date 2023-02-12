import json
import requests
from lxml import etree
url = "http://tool.chinaz.com/subdomain/nua.edu.cn"  #修改最后
headers = {
    "Host": "tool.chinaz.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
response = requests.get(url=url, headers=headers)
tree = etree.HTML(response.text)
url_list = tree.xpath('//div[@class="IcpMain02 SlFenXwrap fl bg-white"]//ul[@class="ResultListWrap"]//div[@class="w23-0 subdomain"]//text()')
for url in url_list:
    print(url)