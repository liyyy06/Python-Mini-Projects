import numpy as np 

btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([btc, gold, spy])
assets_names = ["BTC", "Gold", "SPY"]

returns = []

for i in range(len(assets)):
  initial_price = assets[i, 0]
  print(f"{assets_names[i]}: {initial_price}")
  final_price = assets[i, -1]
  print(f"{assets_names[i]}: {final_price}")
  
  simple_return = (assets[i, -1]-assets[i, 0])/assets[i, 0]
  returns.append(simple_return)
highest = np.argmax(returns)
lowest = np.argmin(returns)
print(f"Highest return asset: {assets_names [highest]}")
print(f"Lowest return asset : {assets_names [lowest]}")
ranking = np.argsort(returns)[::-1]
print("\n===== ASSET RANKING =====")
for i in ranking:
    print(f"{assets_names[i]}: {returns[i] * 100:.2f}%")

port_weight = np.array([0.5, 0.3, 0.2])
port_weight_percent = port_weight*100
port_returns = np.sum(np.array(returns)*port_weight)
print("\n===== PORTFOLIO WEIGHT =====")
for i in range(len(assets)):
  print(f"Portfolio weight    : {assets_names[i]} {port_weight_percent[i]:.0f}%")
print(f"Portfolio returns   : {port_returns*100:.2f}%"