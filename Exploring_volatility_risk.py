import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7) # Using random number (here i'm using seed 7)
mu = 1.08 ** (1/252) - 1 # Stock's expected return
days = 252 * 10 # Period of investation

A = rng.normal (mu, 0.0025, days) # Making random number by using stock's expected return, volatility, and period of investation
B = rng.normal (mu, 0.02, days) 

vol_A_daily = A.std() # Calculating stock's daily volatility (standard deviation)
vol_B_daily = B.std()

vol_A_yearly = vol_A_daily * np.sqrt(252) # Calculating stock's annual volatility (yearly)
vol_B_yearly = vol_B_daily * np.sqrt(252)

print (vol_A_yearly)
print (vol_B_yearly)

ret_A = A.mean() * 252 # Calculating stock's return
ret_B = B.mean() * 252
print(round(ret_A, 3), round(ret_B, 3))

for s in (0.0025, 0.02) : # Making simulation of stocks with different volatility
    r = rng.normal(mu, s, (100000, 252)) # Making 100000 simulation per day in 252 days 
    print (((1+r).prod(1)<1).mean()) # Calculating probability of loss in 252 days

# Visualization
plt.plot(A[:252], label="A") # Stock A visualization, with label 'A'
plt.plot(B[:252], label="B") # Stock B visualization, with label 'B'
plt.title('Daily Return') # Adding title
plt.legend() # Adding legend
plt.show()
