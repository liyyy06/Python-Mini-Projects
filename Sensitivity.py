import numpy as np

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

assets_price = np.array([btc_prices, eth_prices])
assets_name = np.array(["BTC", "ETC"])

covariance = np.cov(eth_prices, btc_prices, ddof=1)[0,1]
if covariance > 0:
    print("BTC dan ETH bergerak searah")
elif covariance < 0:
    print("BTC dan ETH bergerak berlawanan")

slope = (np.cov(eth_prices, btc_prices, ddof=1)[0,1])/np.var(eth_prices)
print(f"Setiap perubahan $1 pada BTC, sensitivitas terhadap ETH adalah {slope:.4f}")