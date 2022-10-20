import asyncio
import time
import telegram
from base64 import decode
import requests
import json
from bs4 import BeautifulSoup


def get_data(stuID, stuPass):
    cookieUrl = 'https://yqtb.nua.edu.cn/mp-czzx/login'
    s = requests.Session()
    # s.cookies.clear
    s.get(cookieUrl, headers={'userId': stuID, 'password': stuPass}, timeout=5)

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '32',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': "idSession=" + s.cookies.get("idSession") + ";openId=" + s.cookies.get("openId") + ";route=" + s.cookies.get("route"),
        'Host': 'yqtb.nua.edu.cn',
        'Origin': 'https://yqtb.nua.edu.cn',
        'Referer': 'https://yqtb.nua.edu.cn/mp-czzx/webs/yqsb/sjhmcj/index.html',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    sourceJson = requests.post('https://yqtb.nua.edu.cn/mp-czzx/dkjl', headers=headers, timeout=5, data={
        'userId': stuID, 'password': stuPass})

    htmlJson = BeautifulSoup(sourceJson.text, "html.parser")
    json_seletc = json.loads(htmlJson.text)

    saveData = {
        'xhOrgh': json_seletc['json']['data']['xhOrgh'],
        'tbrq': '',
        'sffyhz': '0',
        'twqk': '1',
        'sfjc': '0',
        'sfdf': '0',
        'szdf': '2',
        'sfcqglcs': '0',
        'gldd': '',
        'sfhsjc': '2',
        'hsjcjg': '0',
        'jkmqk': '0',
        'xcmqk': '0',
        'lxdh': json_seletc['json']['data']['lxdh'],
        'qtqk': '',
        'role': '1',
        'jrsfwc': '2',
        'ymjzqk': '3',
        'sffx': '0',
        'sfzgfx': '0',
        'jjrStqk': '0',
    }

    id = '未知'
    msg = '错误!'

    # 打卡
    saveData = requests.post(
        'https://yqtb.nua.edu.cn/mp-czzx/save', headers=headers, timeout=5, data=saveData)
    saveJson = BeautifulSoup(saveData.text, "html.parser")
    save_json_seletc = json.loads(saveJson.text)
    sysMsg = json.dumps(save_json_seletc['json'], indent=2).encode(
        'utf-8').decode('unicode_escape')

    if save_json_seletc['json']['data'] == 'true':
        id = json_seletc['json']['data']['xhOrgh']
        msg = '成功！'

    finalMsg = '打卡任务：\n学号:' + id + '\n' + '打卡:' + msg
    # finalMsg = '打卡任务：\n\n学号:' + id + '\n' + '打卡:' + msg + '\n\n' + sysMsg

    return finalMsg


async def main(botToken, message):
    bot = telegram.Bot(botToken)
    async with bot:
        await bot.send_message(text=message, chat_id=395107166)

if __name__ == '__main__':
    botToken = '5426940917:AAGRlAmtYwvkr_3RZrASLoWjoW54s6oMhbU'

    idData = [
        ['梁晨梓', 'M2205118', '205112'],
        ['杨兴远', 'M2205117', '162213'],
        ['徐子为', 'M2205109', '063813'],
    ]

    for i in idData:
        stuID = i[1]
        stuPass = i[2]

        message = i[0] + '\n' + get_data(stuID, stuPass)
        asyncio.run(main(botToken, message))
        print(message + '\n')
        time.sleep(2)
