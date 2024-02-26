import numpy as np
import json


def calculate_ema(data, n=20):
    ema_values = [None] * (n-1)
    k = 2 / (n + 1)
    # Рассчитываем начальное значение EMA как простое скользящее среднее за первые n периодов
    initial_ema = np.mean(data[:n])
    ema_values.append(initial_ema)
    for i in range(n, len(data)):
        ema = (data[i] - ema_values[-1]) * k + ema_values[-1]
        ema_values.append(ema)
    return ema_values


with open('raw_data.json', 'r') as f:
    data = json.load(f)
close_prices = [float(i[4]) for i in data]         # буду считать EMA по ценам закрытия свечи
fast_ema = calculate_ema(close_prices, n=12)
slow_ema = calculate_ema(close_prices, n=26)
macd = [fast_ema[i] - slow_ema[i] if slow_ema[i] else None for i in range(len(data))]
signal = [None] * 25 + calculate_ema(macd[25:], n=9)

result = []
for i in range(len(data)):
    result.append({
        'open': float(data[i][1]),
        'close': float(data[i][4]),
        'high': float(data[i][2]),
        'low': float(data[i][3]),
        'macd': macd[i],
        'signal': signal[i]
    })

with open('macd_data.json', 'w') as f:
    json.dump(result, f)
