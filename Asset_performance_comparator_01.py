import numpy as np

btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([btc, gold, spy])
assets_name = np.array(["BTC", "GOLD", "SPY"])


for i in range(len(assets)):
    print(f"{assets_name[i]}:")
    print(f"Initial price = {assets[i, 0]}")
    print(f"Final price = {assets[i, -1]}")
    print("=" * 15)

returns =[]
for i in range(len(assets)):
    print(f"{assets_name[i]}:")
    simple_return = (assets[i, -1] - assets[i, 0]) / assets[i, 0]
    returns.append(simple_return)
    print(f"Total return = {simple_return * 100}%")    

highest_index = np.argmax(returns)
print(f"Highest performing asset = {assets_name [highest_index]}")
