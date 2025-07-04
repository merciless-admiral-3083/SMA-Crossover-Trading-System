# 📈 SMA Crossover Stock Trading System

This project demonstrates a stock trading strategy based on the Simple Moving Average (SMA) crossover technique. It uses Python, Flask, MySQL, and pandas to analyze stock data, visualize trading signals, and display strategy performance metrics on a web dashboard.

## ✨ Features

- 📥 **Data Import:** Load historical stock data from Excel into a MySQL database.
- 📊 **Strategy Logic:** Calculate 20-day and 50-day SMAs, generate buy/sell signals, and compute returns.
- 📉 **Visualization:** Interactive dashboard showing price, SMAs, buy/sell signals, and key performance metrics.
- 🧪 **Testing:** Unit tests for data validation.

## 📁 Folder Structure

- `data/` — Place your Excel stock data files here.
- `database/`
  - `create_table.sql` — SQL script to create the database and table.
  - `insert_data.py` — Script to import Excel data into MySQL.
- `Strategy/`
  - `moving_average_strategy.py` — Standalone SMA strategy script.
  - `plot_sma_crossover.py` — Standalone plotting script.
  - `strategy_performance.py` — Standalone performance metrics script.
- `templates/`
  - `index.html` — Flask dashboard template.
- `tests/`
  - `test_data_validation.py` — Unit tests for data validation.
- `app.py` — Main Flask application.

## 🚀 Setup Instructions

1. **Install Python dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up MySQL database:**
   ```sh
   mysql -u root -p < database/create_table.sql
   ```
3. **Import stock data:**
   ```sh
   python database/insert_data.py
   ```
4. **Run the Flask web app:**
   ```sh
   python app.py
   ```
   - Open your browser and go to [http://localhost:5000](http://localhost:5000).

5. **(Optional) Run unit tests:**
   ```sh
   python -m unittest discover tests
   ```

## ⚙️ Configuration

- Update MySQL credentials in `app.py` and `database/insert_data.py` if needed.
- Place your Excel data file in the `data` folder.

## 📄 License

This project is for educational purposes and must not be copied.