import numpy as np

print("MULTI-FACTOR BTC RETURN ANALYSIS")

np.random.seed(50)
# 30 returns
sp500 = np.random.normal(
loc = 0.0005,
scale = 0.01,
size = 100)

gold = np.random.normal(
loc = 0.0003,
scale = 0.008,
size = 100)

dxy = np.random.normal(
loc = 0.0001,
scale = 0.005,
size = 100)

interest_rate = np.random.normal(
loc =0,
scale = 0.002,
size = 100)

epsilon = np.random.normal(
loc=0,
scale=0.015,
size=100)

y = (
    0.0002
    + 1.2 * sp500
    + 0.3 * gold
    - 0.8 * dxy
    - 0.5 * interest_rate
    + epsilon
)

z = np.column_stack([epsilon])
x_matrix = np.column_stack([np.ones(len(sp500)),sp500, gold, dxy, interest_rate])

coef = np.linalg.lstsq(x_matrix, y, rcond=None)[0]
print("\nEstimated beta")
print(f"Intercept: {coef[0]}")
print(f"S&P500: {coef[1]}")
print(f"Gold: {coef[2]}")
print(f"DXY: {coef[3]}")
print(f"Interest rate: {coef[4]}")

predict = x_matrix @ coef
print(f"\nMultiple linear regression model: {coef[0]} + {coef[1]}Rsp500 + {coef[2]}Rgold + {coef[3]}Rdxy + {coef[4]} + e")

y = coef[0] + coef[1]*sp500 + coef[2]*gold + coef[3]*dxy + coef[4]*interest_rate + epsilon
y_mean = np.mean(y)
mae = np.mean(np.abs(y-(coef[0]+ coef[1]*sp500 + coef[2]*gold + coef[3]*dxy + coef[4]*interest_rate)))
mse = np.mean((np.abs(y-predict))**2)

sst = np.sum((y-y_mean)**2)
sse = np.sum((y-predict)**2)
ssr = sst - sse
print(f"\nExplained variation: {(ssr/sst)*100:.4f}%")
print(f"Unexplained variation: {(sse/sst)*100:.4f}%")