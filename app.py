from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import mysql.connector
import atexit

app = Flask(__name__)

db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Jaspreet-123',
    database='sma_trading'
)
cursor = db.cursor()

query = "SELECT datetime, close FROM stock_data"
df = pd.read_sql(query, db)

df['datetime'] = pd.to_datetime(df['datetime'])

df['SMA_20'] = df['close'].rolling(window=20).mean()
df['SMA_50'] = df['close'].rolling(window=50).mean()

df['Signal'] = 0
df.loc[df['SMA_20'] > df['SMA_50'], 'Signal'] = 1  
df.loc[df['SMA_20'] < df['SMA_50'], 'Signal'] = -1  

df['Position'] = df['Signal'].shift()

df['Returns'] = df['close'].pct_change()
df['Strategy_Returns'] = df['Returns'] * df['Position']

df['Cumulative_Strategy_Returns'] = (1 + df['Strategy_Returns']).cumprod()
df['Cumulative_Buy_Hold_Returns'] = (1 + df['Returns']).cumprod()

def plot_sma_crossover():
    """Generates a plot of the SMA crossover strategy."""
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

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

@app.route('/')
def index():
    """Renders the dashboard with the strategy visualization."""
    plot_url = plot_sma_crossover()

    total_strategy_return = df['Cumulative_Strategy_Returns'].iloc[-1] - 1
    total_buy_hold_return = df['Cumulative_Buy_Hold_Returns'].iloc[-1] - 1
    sharpe_ratio = df['Strategy_Returns'].mean() / df['Strategy_Returns'].std()
    max_drawdown = (df['Cumulative_Strategy_Returns'] / df['Cumulative_Strategy_Returns'].cummax() - 1).min()

    return render_template('index.html', plot_url=plot_url, 
                           total_strategy_return=total_strategy_return,
                           total_buy_hold_return=total_buy_hold_return,
                           sharpe_ratio=sharpe_ratio,
                           max_drawdown=max_drawdown)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)

def close_db():
    cursor.close()
    db.close()

atexit.register(close_db)
