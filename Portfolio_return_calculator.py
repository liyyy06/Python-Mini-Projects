import numpy as np

# List data
# asset a = 0.5(weight), 0.3(return)
# asset b = 0.3(weight), 0.1(return)
# asset c = 0.2(weight), -0.9(return)

# Saving data into variables
a_weight = 0.5
a_return = 0.3
b_weight = 0.3
b_return = 0.1
c_weight = 0.2
c_return = -0.9

weight = np.array([a_weight, b_weight, c_weight]) # Making list of asset's weight, with total of 3 data
return_asset = np.array([a_return, b_return, c_return]) # Making list of asset's return, with total of 3 data
if len(weight) != len(return_asset): # If the total of weight data is not match with the total of return data, 
    print("Information is not correct") # The program will give output 'Information is not correct'

weight_sum = weight.sum() # Calculating the total of assets weight
if weight_sum != 1: # If the total of assets weight is not 1
    print("Weight value is not matched!") # The program will give output 'Weight value is not matched!'
else : # If the total of assets weight is 1
    print("Weight total: ", weight.sum()*100, "%") # The program will give output '100%' means the weight total of assets is correct

# Calculating the contribution of assets
cont_a = a_return * a_weight 
cont_b = b_return * b_weight
cont_c = c_return * c_weight

total_port = weight @ return_asset # Calculating the total portfolio
print("Return portfolio: ", round(total_port, 20)) # Calculating portfolio's return
print("Return portfolio (percent): ", round(total_port*100, 20), "%") # Return in percent
print(f" Aset A: weight {a_weight}, return {a_return}, contribution {cont_a}") # Showing the summary of assets
print(f" Aset B: weight {b_weight}, return {b_return}, contribution {cont_b}")
print(f" Aset C: weight {c_weight}, return {c_return}, contribution {cont_c}")
