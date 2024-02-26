import requests
import time
import json


symbol = 'BTCUSDT'  # Можете заменить на нужную торговую пару
interval = '15m'
start_time = 1690848000000  # Unix-время начала периода (01.08.2023)
end_time = 1706745600000    # Unix-время окончания периода (01.02.2024)

time_interval = 500 * 15 * 60 * 1000 # 500 интервалов по 15 минут

result = []

while start_time < end_time:
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
        'endTime': start_time + time_interval
    }
    print(start_time)
    response = requests.get('https://fapi.binance.com/fapi/v1/klines', params=params)
    if response.status_code == 200:
        candlestick_data = response.json()
        print(len(candlestick_data), end=' ')
        result.extend(candlestick_data)
        print(len(result))
        '''for candlestick in candlestick_data:
            timestamp = candlestick[0]  # Временная метка свечи
            open_price = candlestick[1]  # Цена открытия свечи
            high_price = candlestick[2]  # Наивысшая цена свечи
            low_price = candlestick[3]  # Низшая цена свечи
            close_price = candlestick[4]  # Цена закрытия свечи
            volume = candlestick[5]  # Объем свечи'''
    else:
        print('Произошла ошибка при выполнении запроса:', response.status_code, response.text)
        break
    time.sleep(5)
    start_time += time_interval
    
    with open('result.json', 'w') as f:
        json.dump(result, f)
