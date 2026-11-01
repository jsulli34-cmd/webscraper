## How to Use

Run the scraper with:
    python3 crypto_prices.py

The program displays the current prices of Bitcoin, Ethereum, and
Solana, along with the time taken to fetch them sequentially and
concurrently.

## Performance Impact

The program uses functional programming with `map()` to apply the same 
function to each cryptocurrency. Using `executor.map` from `ThreadPoolExecutor`
I'm able to apply the same function to multiple cryptocurrencies concurrently.
This allows the program to overlap the time spent waiting for responses and improve performance. In
my test, sequential requests took 0.186 seconds, while concurrent
requests took 0.038 seconds, showing the powerful effect that functional programming
and `concurrent.futures` can have on performance.

<img width="363" height="270" alt="image" src="https://github.com/user-attachments/assets/2d88dd28-670f-4c08-a1a4-79862459f7f5" />
