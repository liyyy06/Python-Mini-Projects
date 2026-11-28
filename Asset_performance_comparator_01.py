import numpy as np

# Making list of price per asset
btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([btc, gold, spy]) # Making list of assets' prices
assets_name = np.array(["BTC", "GOLD", "SPY"]) # Making list of assets' names

# Showing initial and final price of all assets
for i in range(len(assets)):
    print(f"{assets_name[i]}:") 
    print(f"Initial price = {assets[i, 0]}")
    print(f"Final price = {assets[i, -1]}")
    print("=" * 15)

# Calculating simple return of all assets
returns =[] # Making empty list for assets' returns
for i in range(len(assets)): # Looping (3)
    print(f"{assets_name[i]}:") # First, the program will showing the name of the assets
    simple_return = (assets[i, -1] - assets[i, 0]) / assets[i, 0] # Using simple return formula
    returns.append(simple_return) # Adding the results to the empty list
    print(f"Total return = {simple_return * 100}%") # Calculating simple return in percent

highest_index = np.argmax(returns) # Showing asset with highest return
print(f"Highest performing asset = {assets_name [highest_index]}")
