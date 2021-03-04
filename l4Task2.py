from requests import get, utils
from datetime import datetime


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    txt = content.split('</Valute>')
    for cur in txt:
        if code.upper() in cur:
            if code.upper() in cur[cur.find('<CharCode>') + len('<CharCode>'): cur.find('</CharCode>')]:
                a = cur[cur.find('<Value>') + len('<Value>'): cur.find('</Value>')]
                rate_cur = float(a.replace(',', '.'))
                return rate_cur


print(currency_rates('Usd'))
print(currency_rates('eur'))
print(currency_rates('100'))
