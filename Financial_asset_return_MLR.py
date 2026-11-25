import numpy as np

dates = [
    "2025-01", "2025-02", "2025-03",
    "2025-04", "2025-05", "2025-06",
    "2025-07", "2025-08", "2025-09"
]

btc_price = np.array([
    102405.02, 84373.01, 82548.91,
    94207.31, 104638.09, 107135.34,
    115758.20, 108236.71, 114056.09
])

eth_price = np.array([
    3298.26, 2237.90, 1823.48,
    1793.78, 2529.09, 2486.46,
    3696.71, 4390.02, 4145.96
])

spy_price = np.array([
    590.22, 582.73, 550.26,
    545.49, 579.77, 609.57,
    623.60, 636.40, 659.07
])

gold_price = np.array([
    258.56, 263.27, 288.14,
    303.77, 303.60, 304.83,
    302.96, 318.07, 355.47
])

assets = np.array([btc_price, eth_price, spy_price, gold_price])

asset_return = (assets[:, 1:]-assets[:, :-1])/assets[:, :-1]
y_returns = asset_return[0,:]
y = np.column_stack([y_returns])
x_matrix = np.column_stack([np.ones(len(y)), asset_return[1,:], asset_return[2,:], asset_return[3,:]])
coef = np.linalg.lstsq(x_matrix, y, rcond=None)[0]
print("Estimated beta")
print(f"ETH: {coef[1]}")
print(f"SPY: {coef[2]}")
print(f"Gold: {coef[3]}")

print("\nMulti-linear regression model")
print(f"Model: {coef[0].item()} + {coef[1].item()} X1 + {coef[2].item()} X2 + {coef[3].item()} X3 + e")
predict = x_matrix @ coef

print("\nModel analysis")
y_mean = np.mean(y)
mae = np.mean(np.abs(predict-y))
mse = np.mean((y-predict)**2)
print("Mean absolute error: ", mae)
print("Mean squared error: ", mse)

sst = np.sum((y-y_mean)**2)
sse = np.sum((y-predict)**2)
ssr = sst - sse
print(f"Explained variation: {(ssr/sst)*100:.4f}%")
print(f"Unexplained variation: {(sse/sst)*100:.4f}%")

r_squared = ssr/sst
n = len(y)
k = 3
adjusted_r = 1 - (1-r_squared)*((n-1)/(n-k-1))
print(f"Adjusted R-squared: {adjusted_r:.4f}")

print("\nVariables correlation")
x_corr = np.column_stack([asset_return[1], asset_return[2], asset_return[3]])
correlation_var = np.corrcoef(x_corr, rowvar=False)
variables = np.array(["ETH", "SPY", "Gold"])

for i in range(len(variables)):
    for j in range(1+i, len(variables)):
        correlation = correlation_var[i,j]
        print(f"{variables[i]} VS {variables[j]}: {correlation:.4f}")

print("\nVariance inflation factor")
gold_spy_matrix = np.column_stack([np.ones(len(y)), asset_return[2,:], asset_return[3,:]])
eth_spy_matrix = np.column_stack([np.ones(len(y)), asset_return[1,:], asset_return[3,:]])
eth_gold_matrix = np.column_stack([np.ones(len(y)), asset_return[1,:], asset_return[2,:]])
eth_return = asset_return[1,:]
gold_return = asset_return[2,:]
spy_return = asset_return[3,:]

gold_spy = np.linalg.lstsq(gold_spy_matrix, eth_return, rcond=None)[0]
print("Estimated beta")
print("Benchmark = ETH")
print(f"Gold: {gold_spy[1]:.4f}")
print(f"SPY: {gold_spy[2]:.4f}")
eth_mean = np.mean(eth_return)
eth_predict = gold_spy_matrix @ gold_spy
sst = np.sum((eth_return-eth_mean)**2)
sse = np.sum((eth_return-eth_predict)**2)
r_eth = 1 - (sse/sst)
print(f"R-squared: {r_eth:.4f}")
vif_eth = 1/(1-r_eth)
print("VIF: ", vif_eth)

eth_spy = np.linalg.lstsq(eth_spy_matrix, gold_return, rcond=None)[0]
print("\nBenchmark = Gold")
print(f"ETH: {eth_spy[1]:.4f}")
print(f"SPY: {eth_spy[2]:.4f}")
gold_mean = np.mean(gold_return)
gold_predict = eth_spy_matrix @ eth_spy
sst = np.sum((gold_return-gold_mean)**2)
sse = np.sum((gold_return-gold_predict)**2)
r_gold = 1 - (sse/sst)
print(f"R-squared: {r_gold:.4f}")
vif_gold = 1/(1-r_gold)
print("VIF: ", vif_gold)

eth_gold = np.linalg.lstsq(eth_gold_matrix, spy_return, rcond=None)[0]
print("\nBenchmark = SPY")
print(f"Gold: {eth_gold[1]:.4f}")
print(f"SPY: {eth_gold[2]:.4f}")
spy_mean = np.mean(spy_return)
spy_predict = eth_gold_matrix @ eth_gold
sst = np.sum((spy_return-spy_mean)**2)
sse = np.sum((spy_return-spy_predict)**2)
r_spy = 1 - (sse/sst)
print(f"R-squared: {r_spy:.4f}")
vif_spy = 1/(1-r_spy)
print("VIF: ", vif_spy)
