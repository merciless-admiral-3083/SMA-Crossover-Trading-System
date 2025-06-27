import pandas as pd
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='Jaspreet',
    password='Jaspreet-123',
    database='sma_trading'
)
cursor = db.cursor()

query = "SELECT datetime, open, high, low, close, volume FROM stock_data"
df = pd.read_sql(query, db)

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

df.to_csv('strategy_output.csv')

cursor.close()
db.close()
