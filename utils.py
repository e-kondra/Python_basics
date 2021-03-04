from requests import get, utils
from datetime import datetime


def currency_rates(code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    txt = content.split('</Valute>')
    for cur in txt:
        if 'Date' in cur:
            txt_date = cur[cur.find('Date') + len('Date=') + 1: cur.find('Date') + len('Date=') + 11]
            day, month, year = txt_date.split('.')
            date_cur = datetime(year=int(year), month=int(month), day=int(day)).date()
        if code.upper() in cur:
            if code.upper() in cur[cur.find('<CharCode>') + len('<CharCode>'): cur.find('</CharCode>')]:
                a = cur[cur.find('<Value>') + len('<Value>'): cur.find('</Value>')]
                rate_cur = (float(a.replace(',', '.')))
                return date_cur, round(rate_cur, 2)


if __name__ == '__main__':
    date, rate = currency_rates('USD')
    print(f'{rate} {date.isoformat()}')
    date, rate = currency_rates('EUR')

    print(f'{rate} {date.isoformat()}')
