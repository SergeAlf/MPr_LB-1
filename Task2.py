# Завдання №2. Отримати курс валют із сайту НБУ за попередній тиждень з використанням python-бібліотеки requests.

import requests
import datetime

def get_exchange_rate_for_date(date):
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&end={date}&json"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data
            else:
                print(f"Даних для дати {date} не знайдено.")
                return None
        except ValueError:
            print(f"Не вдалося перетворити відповідь у JSON для дати {date}. Відповідь: {response.text}")
            return None
    else:
        print(f"Помилка отримання даних для дати {date}: {response.status_code}")
        return None

def get_exchange_rates_for_last_week():
    today = datetime.date.today()
    last_week_dates = [(today - datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(1, 8)]

    for date in last_week_dates:
        exchange_rates = get_exchange_rate_for_date(date)
        if exchange_rates:
            print(f"Курси валют на {date}:")
            for rate in exchange_rates:
                print(f"{rate['cc']} - {rate['rate']}")
            print("\n")

get_exchange_rates_for_last_week()
