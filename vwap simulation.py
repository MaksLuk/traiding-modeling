import json
import logging
# расчет и анализ индикаторов трейдинга валют и ценных бумаг

with open('vwap_data.json', 'r') as f:
    data = json.load(f)


balance = 1000
bid = 100
leverage = 20
win = 0.02
loose = 0.01

win_count = 0
loose_count = 0
error_count = 0
current = 0

index = 24*4
while index < len(data) - 1:
    if balance < bid:
        print('Баланс опустился ниже ставки')
        break
    if data[index]['vwap'] > data[index]['close']:
        current_price = data[index]['close']
        current = 1
        while index < len(data) - 1:
            index += 1
            if (data[index]['high'] >= current_price * (1 + loose)) and (data[index]['low'] <= current_price * (1 - win)):
                current = 0
                error_count += 1
                break
            if data[index]['high'] >= current_price * (1 + loose):
                current = 0
                loose_count += 1
                balance -= bid * loose * 20
                break
            if data[index]['low'] <= current_price * (1 - win):
                current = 0
                win_count += 1
                balance += bid * win * 20
                break
    elif data[index]['vwap'] < data[index]['close']:
        current_price = data[index]['close']
        current = 1
        while index < len(data) - 1:
            index += 1
            if (data[index]['high'] >= current_price * (1 + win)) and (data[index]['low'] <= current_price * (1 - loose)):
                current = 0
                error_count += 1
                break
            if data[index]['high'] >= current_price * (1 + win):
                current = 0
                win_count += 1
                balance += bid * win * 20
                break
            if data[index]['low'] <= current_price * (1 - loose):
                current = 0
                loose_count += 1
                balance -= bid * loose * 20
                break
    else:
        index += 1


print(f'{balance=}, {win_count=}, {loose_count=}, {error_count=}, {current=}')
