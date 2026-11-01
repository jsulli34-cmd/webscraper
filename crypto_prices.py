#!/usr/bin/env python3

import time
from concurrent.futures import ThreadPoolExecutor

import requests


CRYPTOS = ['BTC', 'ETH', 'SOL']
URL = 'https://api.coinbase.com/v2/prices/{}-USD/spot'


def get_price(crypto):
    response = requests.get(URL.format(crypto), timeout=10)
    response.raise_for_status()

    price = float(response.json()['data']['amount'])
    return crypto, price


def display(prices, elapsed, label):
    print(f'\n{label}:')

    for crypto, price in prices:
        print(f'  {crypto}: ${price:,.2f}')

    print(f'  Time: {elapsed:.3f} seconds')


def main():
    start = time.perf_counter()
    sequential = list(map(get_price, CRYPTOS))
    sequential_time = time.perf_counter() - start

    start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=3) as executor:
        concurrent = list(executor.map(get_price, CRYPTOS))
    concurrent_time = time.perf_counter() - start

    display(sequential, sequential_time, 'Sequential')
    display(concurrent, concurrent_time, 'Concurrent')


if __name__ == '__main__':
    main()
