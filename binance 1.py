import requests
import schedule
import time

def get_top_50_usdt_pairs():
    url = 'https://api.binance.com/api/v3/ticker/24hr'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        top_50_pairs = []
        for pair_data in data:
            if pair_data['symbol'].endswith('USDT'):
                top_50_pairs.append(pair_data)
        return top_50_pairs[:50]
    else:
        print("Failed to fetch data from Binance API")
        return None

def monitor():
    top_50_pairs = get_top_50_usdt_pairs()
    if top_50_pairs:
        top_50_symbols = [pair['symbol'] for pair in top_50_pairs]
        for symbol in top_50_symbols:
            print(symbol)

def main():
    # 每隔一段时间执行一次监控函数
    schedule.every(5).minutes.do(monitor)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
