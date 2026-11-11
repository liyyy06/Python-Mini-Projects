import numpy as np

print("===== PORTFOLIO REBALANCING SIMULATOR =====")
assets_name = np.array(["BTC", "Gold", "SPY"])

initial_prices = np.array([100, 100, 100])
current_prices = np.array([120, 110, 105])

quantities = np.array([50, 30, 20])
target_weights = np.array([0.5, 0.3, 0.2])
value = []

print("\n===== Assets Price =====")
for i in range(len(current_prices)):
    print(f"{assets_name[i]}:")
    print(f"Initial price: {initial_prices[i]}")
    print(f"Current price: {current_prices[i]}")

print("\n===== Current Value =====")
for i in range(len(initial_prices)):
    current_value = current_prices*quantities
    print(f"{assets_name[i]}: {current_prices[i] *quantities[i]}")
    value.append(current_value)
    port_value = np.sum(current_value)
print(f"Portfolio value: {port_value}")

print("\n===== Target Weights =====")
for i in range(len(target_weights)):
    print(f"{assets_name[i]}: {target_weights[i]}")

print("\n===== Target Value =====")
for i in range(len(target_weights)):
    target_value = port_value*target_weights
    print(f"{assets_name[i]}: {target_value[i]}")
    
print("\n===== Rebalancing Amount =====")
for i in range(len(initial_prices)):
    trade = np.abs(target_value - current_value)
    if trade[i] > 0:
        print(f"{assets_name[i]}: Buy {trade[i]}")
    elif trade[i] < 0:
        print(f"{assets_name[i]}: Sell {trade[i]}")
    else:
        print(f"{assets_name[i]}: No transaction")
    