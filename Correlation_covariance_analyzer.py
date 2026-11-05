import numpy as np
from itertools import combinations

asset_1 = np.array([0.02, 0.04, -0.01, 0.03, 0.05])
asset_2 = np.array([0.01, 0.03, -0.02, 0.02, 0.04])
asset_3 = np.array([-0.02, 0.01, 0.03, -0.01, 0.02])

assets = np.array([
    asset_1,
    asset_2,
    asset_3
])

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

    print(f"Asset {i+1} vs Asset {j+1}")
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