import pandas as pd
import numpy as np

df = pd.read_csv('strategy_output.csv')

sharpe_ratio = df['Strategy_Returns'].mean() / df['Strategy_Returns'].std()

df['Cumulative_Max'] = df['Cumulative_Strategy_Returns'].cummax()
df['Drawdown'] = df['Cumulative_Strategy_Returns'] / df['Cumulative_Max'] - 1
max_drawdown = df['Drawdown'].min()

total_strategy_return = df['Cumulative_Strategy_Returns'].iloc[-1] - 1
total_buy_hold_return = df['Cumulative_Buy_Hold_Returns'].iloc[-1] - 1

print("=== Strategy Performance Metrics ===")
print(f"Total Strategy Return: {total_strategy_return:.2%}")
print(f"Total Buy & Hold Return: {total_buy_hold_return:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")
