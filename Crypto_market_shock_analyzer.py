import numpy as np

print("===== CRYPTO MARKET SHOCK ANALYZER =====")
btc_prices = np.array([
    67000, 67500, 67200, 68000,
    68600, 68100, 69000, 69700,
    69300, 70100, 70800, 70400
])

eth_prices = np.array([
    3500, 3540, 3520, 3580,
    3610, 3570, 3650, 3690,
    3660, 3720, 3780, 3750
])

assets = np.array([btc_prices, eth_prices])
assets_name = np.array(["BTC", "ETH"])

btc_simple_return = (btc_prices[1:]-btc_prices[:-1])/btc_prices[:-1]
eth_simple_return = (eth_prices[1:]-eth_prices[:-1])/eth_prices[:-1]

slope = (np.cov(btc_simple_return, eth_simple_return)[0,1])/np.var(eth_simple_return, ddof=1)
print(f"Setiap perubahan return 1% pada ETH, BTC akan bereaksi sebesar {slope:.4f}%")

print("\n=== Perkiraan perubahan BTC terhadap perubahan kecil pada ETH ===")
print(f"Titik referensi : day2")
# day 2 price
btc_day2 = slope*(eth_simple_return[1]-eth_simple_return[0])
print(f"Perkiraan perubahan return BTC di hari kedua {btc_day2}")

btc_2 = btc_simple_return[0] + slope*(eth_simple_return[1]-eth_simple_return[0])
print(f"Perkiraan nilai return BTC di hari kedua {btc_2}")

print("\n=== Regression Model ===")
btc_mean = np.mean(btc_simple_return)
eth_mean = np.mean(eth_simple_return)
intercept = btc_mean - slope*eth_mean
print(f"Model: Y = {intercept} + {slope}X")
hari_2 = intercept + slope*eth_simple_return[1]
print(f"Perkiraan return BTC di hari kedua menggunakan model regression: {hari_2}")

print("\n === Residual Analysis ===")
residual = btc_simple_return[1]-hari_2
print(residual)