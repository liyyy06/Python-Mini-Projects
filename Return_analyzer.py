import numpy as np

print("=====Return Analyzer=====")
price = np.array([100, 105, 103, 109, 118])

print("Initial price: ", price[0])
print("Final price: ", price[-1])

simp_return = ((price[1:] - price[:-1])) / price[:-1]
print("Simple return:")
for i in range(len(simp_return)):
    print(f"Periode {i+1}: {simp_return[i]:.2%}")

total_ret = np.prod(1 + simp_return) - 1
print(f"Total simple return: {total_ret:.2%}")

log_return = np.log(price[1:]/price[:-1])
print("Log return:")
for i in range(len(log_return)):
    print(f"Periode {i+1}: {log_return[i]:.5f}")

ret_log = np.exp(np.sum(log_return)) - 1
print(f"Total return from log: {ret_log:.2%}")

print("Both methods produce the same result:", np.isclose(total_ret, ret_log))

if total_ret > 0:
    print("Performance: Profit")
elif total_ret < 0: 
    print("Performance: Loss")
else:
    print("Performance: -")