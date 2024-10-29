# Завдання №3. Побудувати графік зміни курсів валют за допомогою бібліотеки matplotlib

import requests
import datetime
import matplotlib.pyplot as plt

def get_exchange_rate_for_date(valcode, date):
    url = f"https://bank.gov.ua/NBU_Exchange/exchange_site?start={date}&end={date}&valcode={valcode}&json"
    response = requests.get(url)

    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data[0]  # Повертаємо перший запис з отриманих даних
            else:
                print(f"Даних для валюти {valcode} на дату {date} не знайдено.")
                return None
        except ValueError:
            print(f"Не вдалося перетворити відповідь у JSON для дати {date}. Відповідь: {response.text}")
            return None
    else:
        print(f"Помилка отримання даних для дати {date}: {response.status_code}")
        return None

def get_exchange_rates_for_last_week(valcode):
    today = datetime.date.today()
    last_week_dates = [(today - datetime.timedelta(days=i)).strftime('%Y%m%d') for i in range(1, 8)]
    rates = []

    for date in last_week_dates:
        exchange_rate = get_exchange_rate_for_date(valcode, date)
        if exchange_rate:
            rates.append({'date': date, 'rate': exchange_rate['rate']})

    return rates

def plot_exchange_rates(valcode):
    exchange_rates = get_exchange_rates_for_last_week(valcode)

    if not exchange_rates:
        print(f"Не вдалося отримати дані для валюти {valcode}.")
        return

    dates = [datetime.datetime.strptime(item['date'], '%Y%m%d').date() for item in exchange_rates]
    rates = [float(item['rate']) for item in exchange_rates]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, rates, marker='o', linestyle='-', color='b')
    plt.xlabel('Дата')
    plt.ylabel(f'Курс {valcode}')
    plt.title(f'Зміна курсу {valcode} за попередній тиждень')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

valcode = input("Введіть код валюти (наприклад, USD, EUR): ").upper()
plot_exchange_rates(valcode)