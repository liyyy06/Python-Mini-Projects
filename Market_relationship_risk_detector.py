import numpy as np
from itertools import combinations

btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

weight = np.array([0.5, 0.3, 0.2])

assets = np.array([
    btc,
    gold,
    spy
])

total_return = []

assets_names = ["BTC", "Gold", "SPY"]

for i in range(len(assets)):
    print(f"{assets_names[i]} : {assets[i,0]}")

for i in range(len(assets)):
    log_return = np.log(assets[i, 1:]/assets[i, :-1])
    ret_cum_log = np.exp(np.sum(log_return)) - 1
    print(f"Return {assets_names[i]} : {ret_cum_log:.2%}")
    total_return.append(ret_cum_log)

total_cum_ret= np.sum(total_return * weight)
print(f"Total cummulative return: {total_cum_ret:.2%}")

print("=" * 40)
cov_matrix = np.cov(assets, ddof=1)
cor_matrix = np.corrcoef(assets)
print("Covariance: ")
print(cov_matrix)
print("Correlation: ")
print(cor_matrix)
print("=" * 40)

for i,j in combinations(range(len(assets)), 2):
    cov = np.cov(assets[i], assets[j], ddof=1)[0,1]
    cor = np.corrcoef(assets[i], assets[j])[0,1]

    print(f"{assets_names[i]} vs {assets_names[j]}")
    print(f"Covariance: , {cov:.6f}")
    print(f"Correlation: , {cor:.4f}")

    if cor > 0.7:
        print("Strong Positive")
    elif cor > 0:
        print("Weak Positive")
    elif cor < -0.7:
        print("Strong Negative")
    elif cor < 0:
        print("Weak Negative")
    else:
        print("No Linear Correlation")
    print("=" * 40)