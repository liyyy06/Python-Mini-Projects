import numpy as np

print("=====Risk Dashboard and Outlier Detector=====")

return_asset = np.array([1.5, -0.7, 0.9, 0.5, -0.1])
n = len(return_asset)

mean_ret = return_asset.mean()
print("Rata-rata return asset: ", mean_ret)

std_ret = return_asset.std(ddof=1)
var_ret = std_ret**2
print("Variance: ", var_ret)
print("Standard deviation: ", std_ret)

print("Z-score: ")
z_score = (return_asset-mean_ret)/std_ret
for i in range(len(return_asset)):
    print(f"Asset {i+1}: {z_score[i]}")

outliers = np.abs(z_score) > 2
outliers_assets = []

for i in range(len(outliers)):
    if outliers[i]:
        outliers_assets.append(f"Asset {i+1} ({return_asset[i]}%)")

print("Outliers return: ", outliers_assets)
