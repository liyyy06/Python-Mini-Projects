import numpy as np

# Making list of daily closing prices per asset
btc = np.array([100, 105, 102, 110, 108, 115, 109, 118, 120, 116])
gold = np.array([100, 101, 102, 101, 103, 104, 103, 105, 106, 107])
spy = np.array([100, 102, 101, 104, 105, 107, 106, 109, 110, 112])

assets = np.array([btc, gold, spy]) # Creating list of assets' prices
assets_name = np.array(["BTC", "Gold", "SPY"]) # Creating list of assets name

print("===== Investment Allocation Calculator =====")
total = float(input("Input your total capital: ")) # Input total capital 

print("\n ===== CAPITAL ALLOCATION =====")
total_capital = [] # Making empty list
for i in range(len(assets)): # Looping (3)
    capital = float(input(f"{assets_name[i]} Total capital (USDT): ")) # Input your USDT allocation
    total_capital.append(capital) # Adding your USDT allocation to the empty list

usdt_allocation = np.sum(total_capital) # Calculating your USDT allocation per asset
if total - usdt_allocation != 0: # If the result is not 0, 
    print("The total of USDT is not correct!") # The program will give output 'The total of USDT is not correct!'
else : # If the result is 0,
    percent_allocation = (usdt_allocation/total)*100 # Calculating your USDT allocation
    print(f"Total allocation : {percent_allocation}%") # The program will give output '100%' means all USDT has been used
    unallocated_cap = total - usdt_allocation # Calculating unallocated USDT
    print(f"Unallocated capital: {unallocated_cap} USDT") # The program will give output '0' means you dont have unallocated USDT
    
return_asset = [] # Making empty list for assets return
print("\n===== RETURN ANALYZER =====")
for i in range(len(assets)): # Looping (3)
    # Calculating assets simple return
    returns = (((assets[i, 1:])-(assets[i, :-1]))/assets[i, :-1])*100 # Using simple return formula
    total_return = (np.prod(1 + returns/100)-1)*100 # Calculating total return
    return_asset.append(total_return) # Adding results to the empty list
    print(f"{assets_name[i]}: {total_return:2f}%") # Showing return per asset

highest = np.argmax(return_asset) # Showing asset with highest return
lowest = np.argmin(return_asset) # Showing asset with lowest return
print(f"Highest return: {assets_name [highest]}")
print(f"Lowest return : {assets_name [lowest]}")

print("\n===== PORTFOLIO PROFIT/LOSS =====")
# Calculating portfolio's return
profit_loss = np.array(total_capital)*np.array(total_return)/100
total_profit = np.sum(profit_loss) 

if total_profit > 0: # If the return more than 0,
    print(f"Portfolio profit: {total_profit:.2f} USDT") # Showing portfolio's profit
elif total_profit == 0: # If the return is 0,
    print("No profit or loss") # No profit or loss
else: # If the return less than 0,
    print(f"Portfolio loss: {total_profit:.2f} USDT") # Showing portfolio's loss

# Calculating profit/loss per asset
print("\n===== ASSETS PROFIT/LOSS =====")
for i in range(len(assets)): # Looping(3)
    if profit_loss[i] > 0: # If the return more than 0,
        print(f"{assets_name[i]} profit : {profit_loss[i]}") # Showing asset's profit
    elif profit_loss[i] == 0: # If the return is 0,
        print(f"{assets_name[i]} : no profit or loss") # No profit or loss
    else: # If the return less than 0,
        print(f"{assets_name[i]} loss : {profit_loss[i]}") # Showing asset's loss
    
print("\n===== FINAL PORTFOLIO VALUE =====")
final = total + total_profit # Calculating final portfolio value 
print(f"Final value: {final} USDT") # Showing final portfolio value
