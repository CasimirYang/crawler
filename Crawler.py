import requests
import json


def sendSms(content):
    print(content)


headers = {'Host': 'www.91160.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
           'Origin': 'https://www.91160.com', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest', 'Referer': 'https://www.91160.com/doctors/index/unit_id-21/dep_id-4383/docid-17690.html',
            'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Cookie': '__jsluid=0633205495b49594f6e240cc6b30a960; __guid=SNa62k59227bde6ccb20.19818583; FISKCDDCC=4a44d8f9f1fad83a096cb5529c66a941; LiveWSMBY90996241=1495432159994460184947; LiveWSMBY90996241sessionid=1495432159994460184947; NMBY90996241fistvisitetime=1495432160002; NMBY90996241visitecounts=1; vlstatId=vlstat-1495432160000-2328854289; __jsl_clearance=1495444707.74|0|wOG9LN%2F7iiUBtvcsps9fU1%2B3ZAw%3D; Hm_lvt_c4e8e5b919a5c12647962ea08462e63b=1495432160; Hm_lpvt_c4e8e5b919a5c12647962ea08462e63b=1495444772; ip_city=sz; _ga=GA1.2.1746347604.1495432160; _gid=GA1.2.277007920.1495444819; _gat=1; NMBY90996241LR_cookie_t0=1; NMBY90996241lastvisitetime=1495444818799; NMBY90996241visitepages=15'}

cookies = {'from-my': 'browser', }

payload = {'docid': '17690', 'date': '2017 - 05 - 22', 'days': '6'}
r = requests.post("https://www.91160.com/doctors/ajaxgetclass.html", data=payload, headers=headers, verify=False)
doc = json.loads(r.content).get('sch').get('4383_17690')

docList = list()

docAm = doc.get('4383_17690_am')
docPm = doc.get('4383_17690_pm')

for key in docAm:
    docList.append(docAm.get(key))

for key in docPm:
    docList.append(docPm.get(key))

print(docList)

for item in docList:
    if int(item.get('left_num')) > 0:
        print(item)
        sendSms(item.get('to_date'))


