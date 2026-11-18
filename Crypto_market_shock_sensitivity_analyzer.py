import numpy as np

print("Does Bitcoin's sensitivity to Ethereum change during extreme market movements?")
btc_prices = np.array([
    67000, 67200, 67500, 67300, 67800,
    68100, 67900, 68400, 68200, 68700,
    69000, 68600, 69200, 68800, 69500,
    70100, 70700, 71300, 72000, 72800,
    72200, 71400, 70500, 69800, 69000,
    69500, 70100, 69700, 70400, 71000
])

eth_prices = np.array([
    3500, 3510, 3530, 3520, 3540,
    3560, 3550, 3570, 3560, 3590,
    3610, 3580, 3620, 3590, 3640,
    3690, 3740, 3800, 3860, 3930,
    3870, 3790, 3700, 3630, 3550,
    3590, 3650, 3620, 3680, 3740
])

btc_simple_return = (btc_prices[1:]-btc_prices[:-1])/btc_prices[:-1]
eth_simple_return = (eth_prices[1:]-eth_prices[:-1])/eth_prices[:-1]

slope = np.cov(btc_simple_return, eth_simple_return)[0,1]/np.var(eth_simple_return, ddof=1)
print(f"\nPerubahan return sebesar 1 percentage point pada ETH, BTC akan bereaksi sebesar {slope:.4f} percentage point")

btc_30_return = slope*(eth_simple_return[-1])
print(f"\nPrediksi perubahan return BTC di hari ke-30: {btc_30_return*100:.3f}%")

btc_30_return_value = (btc_simple_return[-1] + slope*(eth_simple_return[-1]-eth_simple_return[-2]))
print(f"\nPrediksi nilai return BTC di hari ke-30: {btc_30_return_value*100:.3f}%")

print("\n=== Regression Model ===")
btc_return_mean = np.mean(btc_simple_return)
eth_return_mean = np.mean(eth_simple_return)
intercept = btc_return_mean - slope*eth_return_mean
print(f"Model: {intercept:4f} + {slope:4f}X")

print(f"Prediksi return BTC hari ke 30 dengan model: {intercept+slope*eth_simple_return[-1]:.4f}")

print("Model Error Analysis")
residual = btc_simple_return[-1]-(intercept+slope*eth_simple_return[-1])
print(f"Residual: {residual:.4f}")

btc_positive_shock = btc_simple_return[eth_simple_return > 0.015]
eth_positive_shock = eth_simple_return[eth_simple_return > 0.015]
btc_negative_shock = btc_simple_return[eth_simple_return < -0.015]
eth_negative_shock = eth_simple_return[eth_simple_return < -0.015] 

normal_mask = (eth_simple_return >= -0.015) & (eth_simple_return <= 0.015)  
btc_normal_shock = btc_simple_return[normal_mask]
eth_normal_shock = eth_simple_return[normal_mask]

print(f"\nThreshold 1.5%")
print("\nPositive Shock:", len(eth_positive_shock))
print("Negative Shock:", len(eth_negative_shock))
print("Normal Market:", len(eth_normal_shock))

btc_mean_positive = np.mean(btc_positive_shock)
btc_mean_negative = np.mean(btc_negative_shock)
eth_mean_positive = np.mean(eth_positive_shock)
eth_mean_negative = np.mean(eth_negative_shock)
btc_mean_normal = np.mean(btc_normal_shock)
eth_mean_normal = np.mean(eth_normal_shock)

print(f"\nPositive shock")
print(f"Rata-rata return BTC: {btc_mean_positive*100:.3f}%")
print(f"Rata-rata return ETH: {eth_mean_positive*100:.3f}%")

print(f"\nNegative shock")
print(f"Rata-rata return BTC: {btc_mean_negative*100:.3f}%")
print(f"Rata-rata return ETH: {eth_mean_negative*100:.3f}%")

print(f"\nNormal market")
print(f"Rata-rata return BTC: {btc_mean_normal*100:.3f}%")
print(f"Rata-rata return ETH: {eth_mean_normal*100:.3f}%")