import requests
import json

BSite = [{'一号场地': 'c4e76dab6c9549949fb8184358f589c9'},
    {'二号场地': 'lOWHwILmwNocv15rXkvqODBAXNuqGPTn'},
    {'三号场地': '9Ja4dT8ZBn73Q9on9LfExSRU6CWcnRIb'},
    {'四号场地': 'YCoA2D6GsJJxLwxGZ7PtPnJ449BLYbXm'},
    {'五号场地': 'a972TpWf3NHRhVyHdq1EB6LlJ1wG1MEV'},
    {'六号场地': 'v8MjefSF1y6MMvqoJ86L3lxmWdSAV17d'}]
# 遍历字典
for key in BSite:
    # 获取场地名
    for name in key:
        # 获取场地ID
        print(name)
        for id in key.values():
            # 获取场地状态
            # print(id)
            try:
                # 请求场地状态
                url = 'https://ssts.nua.edu.cn/yygj/yygj/common/post/checkYysjd?cd=' + id + '&yysjd=18:00~19:00'
                # Cookie
                cookies = {
                    'fwgjxt': '0ab45e8f-ed92-49b9-bcd8-ff40db02c215',
                    'kisso': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxMDAwIiwiaXAiOiIxMC4xMi42OS4xNSIsImlzcyI6Ik0yMjA1MTAxIiwiaWF0IjoxNjY4MDY1OTQ2fQ.qtu_c3sYGdMDGz-zFNeA1J3o41dN9WmcSLIta5CGtWkfs90BdhNUFhx-Wjk8kIsUbu75gHYr8K-gwXJ4fVmZnA',
                }
                # 请求头
                headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
                    'Connection': 'keep-alive',
                    'Origin': 'https://ssts.nua.edu.cn',
                    'Referer': 'https://ssts.nua.edu.cn/yygj/form/instance/mobile/add?definationId=231b1825ba7542079fcc08d462757084&processKey=ymqcdsq&auth=231b1825ba7542079fcc08d462757084_LAUNCH&backFlag=noBack&isMobile=true',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest',
                    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                }
                response = requests.post(url=url, cookies=cookies, headers=headers)
                json_seletc = json.loads(response.text)
                if json_seletc["count"] == 0:
                    print('可以预约')
                elif json_seletc["count"] == 1:
                    print('不可预约')
            except Exception as e:
                print(e)