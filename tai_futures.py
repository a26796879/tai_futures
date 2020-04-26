import requests, wget, time, datetime
from bs4 import BeautifulSoup

def get_price(url):
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.3.517014540.1567243392; _gid=GA1.3.745833474.1587831730; lt=60B9C15256575922565857594543D430C6D8474B514E512457514E5153554E2059486050C45558225754575150565020C35155C2C4555620C657505452565220C4C65556C3C657204041413040404228B659C84C5742403F434044C0C945D130A2565C2500; ASP.NET_SessionId=xmgwvmu1xzwnyfk0btc4kt12; BIGipServerPOOL_INFO512_NEWINFO_TCP_80=1393954988.20480.0000',
    'Host': 'info512.taifex.com.tw',
    'Origin': 'https://info512.taifex.com.tw',
    'Referer': 'https://info512.taifex.com.tw/Future/FusaQuote_Norl.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'X-MicrosoftAjax': 'Delta=true',
    'X-Requested-With': 'XMLHttpRequest'
    }
    parser = {
    'ctl00$ScriptManager1': 'ctl00$ContentPlaceHolder1$UpdatePanel2|ctl00$ContentPlaceHolder1$Timer1',
    'ctl00_ScriptManager1_HiddenField': ';;AjaxControlToolkit, Version=1.0.10618.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:zh-TW:43a0de04-5dca-41f9-a426-313ba06240d5:411fea1c:865923e8:e7c87f07:91bd373d:bbfda34c:30a78ec5:3510d9fc;',
    'ctl00$ContentPlaceHolder1$cbxRefresh': 'on',
    'ctl00$ContentPlaceHolder1$ddlFusa_Commodity': 'TX',
    'ctl00$ContentPlaceHolder1$ddlFusa_SelMon': '202005',
    'hiddenInputToUpdateATBuffer_CommonToolkitScripts': '1',
    '__EVENTTARGET': 'ctl00$ContentPlaceHolder1$Timer1',
    '__VIEWSTATE': '/wEPBRI2MzcyMzUyMTQ1NjY2NDYwNzlkL/TMvgULRmuw5MqR4vPAE/ZZSvDx68C6uo1lGy8sVOc=',
    '__VIEWSTATEGENERATOR': '56A1EE3B',
    '__ASYNCPOST': 'true'
    }
    res = requests.post(url, headers = headers , params = parser)
    soup = BeautifulSoup(res.text, 'lxml')
    tag = soup.select("#ctl00_ContentPlaceHolder1_uc_DgFusaQuote1_dgData")
    taifex_close = tag[0].find_all("tr", class_="custDataGridRow")[2]
    #print (future.find_all('td'))
    now_price = taifex_close.find_all('td')[6].text
    #即時報價
    print (now_price)

#morning_start = datetime(2017, 6, 20, 19, 11, 12, 926763)
#morning_end = datetime(2017,)

for a in range(10):
    get_price('https://info512.taifex.com.tw/future/fusaquote_norl.aspx')
    get_price('https://info512ah.taifex.com.tw/Future/FusaQuote_Norl.aspx')

#現在時間
#print (taifex_close.find_all('td')[14].text)


#print (datetime.datetime.now())
