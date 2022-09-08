import requests, re, json
from bs4 import BeautifulSoup

# Config

Ali1USDPageURL = 'https://aliexpress.ru/item/32892046259.html'
CBRFApiSiteURL = 'https://www.cbr-xml-daily.ru/daily_json.js'
MetricServerURL = 'http://192.168.0.100:8428/'

KursAli = ""
KursCBRF = ""

# Ali

site = requests.get(Ali1USDPageURL)

if (site.status_code != 200):
    print("Ali request error: " + str(site.status_code))
    exit()

soup = BeautifulSoup(site.text, "html.parser")

for tag in soup.find_all("span", class_="product-price-current"):
    KursAli = (''.join(x for x in tag.text if (x.isdigit() or x == ','))).replace(',','.')
    
print("Курс Ali: " + KursAli)

# ЦБ РФ

site = requests.get(CBRFApiSiteURL)

if (site.status_code != 200):
    print("Kurs request error: " + str(site.status_code))
    exit()

KursCBRF = str(json.loads(site.text)["Valute"]["USD"]["Value"])
print("Курс ЦБ РФ: " + KursCBRF)

# Send metrics ↓

url = MetricServerURL + 'api/v1/import/csv?format=1:label:source,2:metric:exchange_usd_rub'

if KursCBRF != '':
    x = requests.post(url, "Central Bank Of Russia," + KursCBRF)
    if (x.status_code != 200 and x.status_code != 204):
        print("Не удалось отправить метрику: " + str(x.status_code))
else:
    print("Курс ЦБ РФ пуст")

if KursAli != '':
    x = requests.post(url, "AliExpress," + KursAli)
    if (x.status_code != 200 and x.status_code != 204):
        print("Не удалось отправить метрику: " + str(x.status_code))
else:
    print("Курс Али пуст")