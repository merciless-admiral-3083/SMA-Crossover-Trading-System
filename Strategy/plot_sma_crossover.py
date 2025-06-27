import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('strategy_output.csv')

df['datetime'] = pd.to_datetime(df['datetime'])

df.dropna(subset=['SMA_20', 'SMA_50'], inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df['close'], label='Close Price', color='blue', linewidth=1)
plt.plot(df['datetime'], df['SMA_20'], label='20-day SMA', color='red', linestyle='dashed')
plt.plot(df['datetime'], df['SMA_50'], label='50-day SMA', color='green', linestyle='dotted')

plt.scatter(df[df['Signal'] == 1]['datetime'], df[df['Signal'] == 1]['close'], marker='^', color='green', label='Buy Signal', alpha=1, edgecolors='black')
plt.scatter(df[df['Signal'] == -1]['datetime'], df[df['Signal'] == -1]['close'], marker='v', color='red', label='Sell Signal', alpha=1, edgecolors='black')

plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("SMA Crossover Trading Strategy")
plt.legend()
plt.grid()
plt.show()
