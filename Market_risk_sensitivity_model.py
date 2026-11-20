import numpy as np
print("How sensitive is this stock to movements in the overall market, and does its market risk change over time?")

np.random.seed(42)

# 40 daily market returns
market_returns = np.random.normal(
    loc=0.0005,
    scale=0.01,
    size=40
)

# Two different market sensitivity regimes
beta_1 = 0.7
beta_2 = 1.5

beta = np.concatenate([
    np.full(20, beta_1),
    np.full(20, beta_2)
])

# Random stock-specific movements
epsilon = np.random.normal(
    loc=0,
    scale=0.008,
    size=40
)

alpha = 0.0002

# Stock returns
stock_returns = (
    alpha
    + beta * market_returns
    + epsilon
)

returns = np.array([market_returns, stock_returns])

print("\nStatic beta estimation")
betas = np.cov(stock_returns, market_returns)[0,1]/np.var(market_returns, ddof=1)
mean_stock = np.mean(stock_returns)
mean_market = np.mean(market_returns)
intercept = mean_stock - betas*mean_market
print(f"Linear regression model: {intercept:.4f} + {betas:.4f}X")

residual = stock_returns -  (intercept + betas*market_returns)
abs_residual = np.abs(stock_returns -  (intercept + betas*market_returns))
residual_mean = np.mean(residual)
residual_mean_abs = np.mean(abs_residual)
squared_residual = (stock_returns -  intercept + betas*market_returns)**2
squared_residual_mean = np.mean(squared_residual)
print(f"Rata-rata residual model: {residual_mean}")
print(f"Mean absolute residual: {residual_mean_abs}")
print(f"Mean squared residual: {squared_residual_mean}")

sst = np.sum((stock_returns - mean_stock)**2)
sse = np.sum((stock_returns - (intercept + betas*market_returns))**2)
r_squared = 1 - (sse/sst)
ssr = sst-sse
print(f"Actual return variation yang dijelaskan model: {r_squared}")
print(f"Unexplained variation: {(sse/sst)*100:.4f}%")
print(f"Explained variation: {(ssr/sst)*100:.4f}%")