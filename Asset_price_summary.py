import numpy as np

btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([105, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([
    btc,
    gold,
    spy
])

assets_names = ["BTC", "Gold", "SPY"]

print("=====Asset Price Summary=====")
for i in range(len(assets)):
    print(f"{assets_names [i]}: ")
    print(f"Initial Price: {assets[i,0]}")
    print(f"Final Price: {assets[i, -1]}")
    print("=" * 20)