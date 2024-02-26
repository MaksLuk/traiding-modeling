import numpy as np
import json


def calculate_ema(data, n=20):
    ema_values = [None for _ in range(n-1)]
    k = 2 / (n + 1)
    initial_ema = np.mean(data[:n]) # Рассчитываем начальное EMA
    ema_values.append(initial_ema)
    for i in range(n, len(data)):
        ema =  ema_values[-1] + k*(data[i] - ema_values[-1])
        ema_values.append(ema)
    return ema_values


with open('result.json', 'r') as f:
    data = json.load(f)
close_prices = [float(i[4]) for i in data]         # буду считать EMA по ценам закрытия свечи
ema_values = calculate_ema(close_prices)

result = []
for i in range(len(data)):
    result.append({
        'open': float(data[i][1]),
        'close': float(data[i][4]),
        'high': float(data[i][2]),
        'low': float(data[i][3]),
        'ema': ema_values[i]
    })

with open('data.json', 'w') as f:
    json.dump(result, f)
