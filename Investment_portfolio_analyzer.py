import numpy as np

btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([btc, gold, spy])
assets_name = np.array(["BTC", "Gold", "SPY"])

print("===== Investment Allocation Calculator =====")
total = float(input("Input your total capital: "))

print("\n ===== CAPITAL ALLOCATION =====")
total_capital = []
for i in range(len(assets)):
    capital = float(input(f"{assets_name[i]} Total capital (USDT): "))
    total_capital.append(capital)

usdt_allocation = np.sum(total_capital)
if total - usdt_allocation != 0:
    print("Jumlah USDT tidak sesuai!")
else : 
    percent_allocation = (usdt_allocation/total)*100
    print(f"Total allocation : {percent_allocation}%") 
    unallocated_cap = total - usdt_allocation
    print(f"Unallocated capital: {unallocated_cap} USDT")
    
return_asset = []
print("\n===== RETURN ANALYZER =====")
for i in range(len(assets)):
    returns = (((assets[i, 1:])-(assets[i, :-1]))/assets[i, :-1])*100
    total_return = (np.prod(
    1 + returns/100)-1)*100
    return_asset.append(total_return)
    print(f"{assets_name[i]}: {total_return:2f}%")

highest = np.argmax(return_asset)
lowest = np.argmin(return_asset)
print(f"Highest return: {assets_name [highest]}")
print(f"Lowest return : {assets_name [lowest]}")

print("\n===== PORTFOLIO PROFIT/LOSS =====")
profit_loss = np.array(total_capital)*np.array(total_return)/100
total_profit = np.sum(profit_loss)

if total_profit > 0:
    print(f"Portfolio profit: {total_profit:.2f} USDT")
elif total_profit == 0:
    print("No profit or loss")
else:
    print(f"Portfolio loss: {total_profit:.2f} USDT")
    
print("\n===== ASSETS PROFIT/LOSS =====")
for i in range(len(assets)):
    if profit_loss[i] > 0:
        print(f"{assets_name[i]} profit : {profit_loss[i]}")
    elif profit_loss[i] == 0: 
        print(f"{assets_name[i]} : no profit or loss")
    else:
        print(f"{assets_name[i]} loss : {profit_loss[i]}")
    
print("\n===== FINAL PORTFOLIO VALUE =====")
final = total + total_profit
print(f"Final value: {final} USDT")