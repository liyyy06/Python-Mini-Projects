import numpy as np
from itertools import combinations

# List of assets price
asset_1 = np.array([0.02, 0.04, -0.01, 0.03, 0.05])
asset_2 = np.array([0.01, 0.03, -0.02, 0.02, 0.04])
asset_3 = np.array([-0.02, 0.01, 0.03, -0.01, 0.02])

# List of assets
assets = np.array([
    asset_1,
    asset_2,
    asset_3
])

cov_matrix = np.cov(assets, ddof=1) # Calculating assets covariance
cor_matrix = np.corrcoef(assets) # Calculating assers correlation
print("Covariance: ")
print(cov_matrix)
print("Correlation: ")
print(cor_matrix)
print("=" * 40)

# Make combinations of 2 from 3 assets
for i,j in combinations(range(len(assets)), 2):
    cov = np.cov(assets[i], assets[j], ddof=1)[0,1] # Covariance 
    cor = np.corrcoef(assets[i], assets[j])[0,1] # Correlation

    print(f"Asset {i+1} vs Asset {j+1}") # Assets combination
    print(f"Covariance: , {cov:.6f}") # Print assets covariance 
    print(f"Correlation: , {cor:.4f}") # Print assets correlation

    if cor > 0.7: # If the correlation more than 0.7, the assets showing strong positive linear relationship
        print("Strong Positive")  
    elif cor > 0: # If the correlation between 0.7 and 0, the assets showing weak positive linear relationship
        print("Weak Positive")
    elif cor < -0.7: # If the correlation less than -0.7, the assets showing strong negative linear relationship
        print("Strong Negative")
    elif cor < 0: # If the correlation between -0.7 and 0 the assets showing weak negative linear relationship
        print("Weak Negative")
    else:
        print("No Linear Correlation") # If the correlation is 0, the assets do not have linear relationship
    print("=" * 40)
