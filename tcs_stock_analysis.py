# Task 1: TCS Stock Market Data Analysis
# Algorithm + Database Code
# No yfinance required

import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create stock database manually
tcs_data = {
    "Date": [
        "2024-01-01", "2024-02-01", "2024-03-01",
        "2024-04-01", "2024-05-01", "2024-06-01",
        "2024-07-01", "2024-08-01", "2024-09-01",
        "2024-10-01", "2024-11-01", "2024-12-01"
    ],
    "Open": [
        3800, 3850, 3920, 3980, 4100, 4150,
        4200, 4250, 4300, 4180, 4220, 4350
    ],
    "High": [
        3900, 3950, 4050, 4120, 4200, 4280,
        4320, 4380, 4400, 4300, 4360, 4450
    ],
    "Low": [
        3750, 3800, 3880, 3950, 4050, 4100,
        4150, 4200, 4250, 4100, 4180, 4300
    ],
    "Close": [
        3850, 3920, 4000, 4100, 4150, 4220,
        4280, 4320, 4260, 4200, 4340, 4400
    ],
    "Volume": [
        1200000, 1350000, 1500000, 1450000, 1600000, 1750000,
        1800000, 2000000, 1900000, 1700000, 2100000, 2300000
    ]
}

# Step 2: Convert database into DataFrame
data = pd.DataFrame(tcs_data)

# Step 3: Convert Date column into date format
data["Date"] = pd.to_datetime(data["Date"])

# Step 4: Calculate Daily Return
data["Daily Return"] = data["Close"].pct_change() * 100

# Step 5: Calculate Moving Average
data["3 Month MA"] = data["Close"].rolling(window=3).mean()

# Step 6: Find highest price, lowest price, and highest volume
highest_price = data.loc[data["High"].idxmax()]
lowest_price = data.loc[data["Low"].idxmin()]
highest_volume = data.loc[data["Volume"].idxmax()]

# Step 7: Print database
print("TCS Stock Database:")
print(data)

# Step 8: Print insights
print("\nKey Insights:")
print("Highest Price Date:", highest_price["Date"])
print("Highest Price:", highest_price["High"])

print("Lowest Price Date:", lowest_price["Date"])
print("Lowest Price:", lowest_price["Low"])

print("Highest Volume Date:", highest_volume["Date"])
print("Highest Volume:", highest_volume["Volume"])

# Step 9: Trend analysis
first_close = data["Close"].iloc[0]
last_close = data["Close"].iloc[-1]

if last_close > first_close:
    print("\nOverall Trend: Bullish")
else:
    print("\nOverall Trend: Bearish")

# Step 10: Closing price graph
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Close"], marker="o", label="Closing Price")
plt.title("TCS Closing Price Analysis")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.legend()
plt.grid(True)
plt.show()

# Step 11: Moving average graph
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Close"], marker="o", label="Closing Price")
plt.plot(data["Date"], data["3 Month MA"], marker="o", label="3 Month Moving Average")
plt.title("TCS Moving Average Analysis")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# Step 12: Volume graph
plt.figure(figsize=(10, 5))
plt.bar(data["Date"], data["Volume"])
plt.title("TCS Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid(True)
plt.show()
