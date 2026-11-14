import numpy as np

days = np.array([1, 2, 3, 4, 5, 6, 7])

btc_price = np.array([
    60000,
    61200,
    60800,
    62500,
    63000,
    62100,
    64000
])
h=1
print("\n===== SLOPE ANALYZER =====")
for i in range(6):
    slope = np.diff(btc_price) / np.diff(days)
    print(f"Periode {i+1}: {slope[i]}")

print("\n===== FINITE DIFFERENCE ANALYZER =====")
print("===== Forward Difference =====")
for i in range(len(btc_price)-1):
    forward_diff = btc_price[i+1]-btc_price[i]
    print(f"Day {i}: {forward_diff}")

print("\n===== Backward Difference =====")
for i in range(1, len(btc_price)):
    backward_diff = btc_price[i]-btc_price[i-1]
    print(f"Day {i}: {backward_diff}")

print("\n===== Central Difference =====")
for i in range(1, len(btc_price)-1):
    central_diff = (btc_price[i+1]-btc_price[i-1])/2
    print(f"Day {i}: {central_diff}")

print("\n===== TAYLOR ESTIMATION =====")
print(f"Current BTC price: {btc_price[-1]}")
price = btc_price[-1]
derivative = btc_price[-1]-btc_price[5]
h = 1
estimated = price + derivative * h
print(f"Estimated BTC price on day 8: {estimated}")