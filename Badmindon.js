{pid: "c4e76dab6c9549949fb8184358f589c9", ymqcdmc: "一号场地"}
{pid: "lOWHwILmwNocv15rXkvqODBAXNuqGPTn", ymqcdmc: "二号场地"}
{pid: "9Ja4dT8ZBn73Q9on9LfExSRU6CWcnRIb", ymqcdmc: "三号场地"}
{pid: "YCoA2D6GsJJxLwxGZ7PtPnJ449BLYbXm", ymqcdmc: "四号场地"}
{pid: "a972TpWf3NHRhVyHdq1EB6LlJ1wG1MEV", ymqcdmc: "五号场地"}
{pid: "v8MjefSF1y6MMvqoJ86L3lxmWdSAV17d", ymqcdmc: "六号场地"}

curl 'https://ssts.nua.edu.cn/yygj/form/defination/api/saveFormData' \
  -H 'Accept: */*' \
  -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json;charset=UTF-8' \
  -H 'Cookie: fwgjxt=0ab45e8f-ed92-49b9-bcd8-ff40db02c215; kisso=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiIxMDAwIiwiaXAiOiIxMC4xMi42OS4xNSIsImlzcyI6Ik0yMjA1MTAxIiwiaWF0IjoxNjY4MDY1OTQ2fQ.qtu_c3sYGdMDGz-zFNeA1J3o41dN9WmcSLIta5CGtWkfs90BdhNUFhx-Wjk8kIsUbu75gHYr8K-gwXJ4fVmZnA' \
  -H 'Origin: https://ssts.nua.edu.cn' \
  -H 'Referer: https://ssts.nua.edu.cn/yygj/form/instance/mobile/add?definationId=231b1825ba7542079fcc08d462757084&processKey=ymqcdsq&auth=231b1825ba7542079fcc08d462757084_LAUNCH&backFlag=noBack&isMobile=true' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw '
    {"mainCode":"T_YMQ_SQ",
    "$field101":"字段自动带出",
    "T_YMQ_SQ$SQRQ":"2022-11-10 15:44:18",
    "T_YMQ_SQ$SQRQhong":"#currDate#",
    "T_YMQ_SQ$CJRQ":"2022-11-10 15:44:22",
    "T_YMQ_SQ$CJRQhong":"#currDate#",
    "T_YMQ_SQ$SQR":"董兴杭",
    "T_YMQ_SQ$SQRhong":"#userName#",
    "T_YMQ_SQ$XQ":"星期四",
    "T_YMQ_SQ$XQhong":"#xq#",
    "sqlYMQCD":"",
    "T_YMQ_SQ$YMQCD":"YCoA2D6GsJJxLwxGZ7PtPnJ449BLYbXm",
    "selectT_YMQ_SQ$YMQCD":"",
    "CurIndexT_YMQ_SQ$YMQCD":[],
    "flagT_YMQ_SQ$YMQCD":"1",
    "midSelectLabelT_YMQ_SQ$YMQCD":[],
    "midSelectValT_YMQ_SQ$YMQCD":[],
    "activeSelect$T_YMQ_SQ$YMQCD":"YCoA2D6GsJJxLwxGZ7PtPnJ449BLYbXm",
    "sqlYYSJD":"",
    "T_YMQ_SQ$YYSJD":"18:00~19:00",
    "selectT_YMQ_SQ$YYSJD":"",
    "CurIndexT_YMQ_SQ$YYSJD":[],
    "flagT_YMQ_SQ$YYSJD":"",
    "midSelectLabelT_YMQ_SQ$YYSJD":[],
    "midSelectValT_YMQ_SQ$YYSJD":[],
    "activeSelect$T_YMQ_SQ$YYSJD":"18:00~19:00",
    "T_YMQ_SQ$SYRS":4,
    "toUper$SYRS":"肆元整",
    "T_YMQ_SQ$SQSY":"",
    "$field1001":2,
    "$field1001hong":"#ymqyysycs#",
    "$本周内剩余次数":null,
    "undefined":{},
    "buildformId":"2de5657e1f8049b8852cb22bf3c2c6c1",
    "definationId":"231b1825ba7542079fcc08d462757084",
    "mainId":"xSCBKfT6p5MCLEyBDp8W44m6mM737h81",
    "processKey":"ymqcdsq(v2)",
    "taskId":"",
    "T_YMQ_SQ$YMQCD$label":"四号场地",
    "T_YMQ_SQ$YYSJD$label":"18:00~19:00",
    "subData":{},
    "selectAssignMap":{},
    "isCreate":true,
    "isStaging":false,
    "authId":"231b1825ba7542079fcc08d462757084_LAUNCH"}' \
  --compressed