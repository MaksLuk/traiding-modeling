import numpy as np
import json


def calculate_vwap(data):
    period = 24*4   # период - сутки
    avg_prices = [ ( float(i[2]) + float(i[3]) + float(i[4]) )/3 for i in data]
    vwap = [None] * period
    for i in range(period, len(data)):
        sum_price_and_volume = 0
        sum_volume = 0
        for j in range(i - period, i+1):
            sum_volume += float(data[i-j][5])
            sum_price_and_volume += float(data[i-j][5]) * avg_prices[i-j]
        vwap.append(sum_price_and_volume / sum_volume)
    return vwap


with open('raw_data.json', 'r') as f:
    data = json.load(f)
vwap = calculate_vwap(data)

result = []
for i in range(len(data)):
    result.append({
        'open': float(data[i][1]),
        'close': float(data[i][4]),
        'high': float(data[i][2]),
        'low': float(data[i][3]),
        'vwap': vwap[i]
    })

with open('vwap_data.json', 'w') as f:
    json.dump(result, f)
