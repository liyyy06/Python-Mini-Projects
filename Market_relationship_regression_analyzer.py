import numpy as np

spy_returns = np.array([0.5, -0.3, 0.8, 0.2, -0.6, 1.0, -0.2, 0.4, 0.7, -0.5])

btc_returns = np.array([1.2, -0.8, 1.5, 0.6, -1.0, 2.0, -0.3, 0.9, 1.4, -0.7])
assets = np.array([spy_returns, btc_returns])
print("===== Can SPY returns help explain BTC returns? =====")
n = len(spy_returns)

print("\n# Covariance check")
spy_mean = np.mean(spy_returns)
btc_mean = np.mean(btc_returns)
cov = np.sum((spy_returns - spy_mean)*(btc_returns - btc_mean))/(n-1)
if cov > 0:
    print(f"BTC dan SPY bergerak searah: Covariance {cov}")
elif cov < 0:
    print(f"BTC dan SPY bergerak berlawanan: Covariance {cov}")
else:
    print(f"BTC dan SPY tidak menunjukkan hubungan linear dalam ukuan covariance! Covariance {cov}")

print("\n# Correlation check")
spy_std = np.std(spy_returns, ddof=1)
btc_std = np.std(btc_returns, ddof=1)
cor = cov/(spy_std*btc_std)
if cor == -1:
    print(f"BTC dan SPY menunjukkan Perfect Negative Correlation")
elif cor < 0:
    print(f"BTC dan SPY menunjukkan hubungan linear negatif kuat")
elif cor == 0:
    print(f"BTC dan SPY tidak memiliki hubungan linear")
elif cor == 1:
    print(f"BTC dan SPY menunjukkan Perfect Positive Correlation")
elif cor > 0:
    print(f"BTC dan SPY menunjukkan hubungan linear positif kuat")

print("\n# Linear Regression")
reg_slope1 = np.sum((spy_returns-spy_mean)*(btc_returns-btc_mean))
reg_slope2 = np.sum((spy_returns-spy_mean)**2)
reg_slope = reg_slope1/reg_slope2
intcept = btc_mean - (reg_slope*spy_mean)
print(f"Linear regression: {intcept:.4f} + {reg_slope:.4f}X")

print("\n# Residual Analysis")
def reg(x):
    return intcept + reg_slope*x
btc_predicted = reg(spy_returns)
residual = btc_returns - btc_predicted
mean_res = np.mean(residual)
if mean_res > 0:
    print("Model cenderung underpredict")
elif mean_res < 0:
    print("Model cenderung underpredict")
mean_abs_res = np.mean(np.abs(residual))
print("Mean absolute residual: ", round(mean_abs_res, 4))
res_max = np.max(np.abs(residual))
print("Kesalahan prediksi dengan residu terbesar: ", round(res_max, 4))

# model evaluation
ss_res = np.sum(residual**2)
ss_tot = np.sum((btc_returns - btc_mean)**2)
r_squared = 1 - (ss_res / ss_tot)
mae = np.mean(np.abs(residual))
rmse = np.sqrt(np.mean(residual**2))
print("Model dapat menjelaskan", round(r_squared*100,2),"% variasi return BTC dalam dataset")
print("Rata-rata kesalahan prediksi BTC return menggunakan model Linear Regression: ", round(mae,2), "%")
print("Besar kesalahan prediksi dengan memperhitungkan penalti lebih besar untuk error ekstrem: ", round(rmse,2), "%")
