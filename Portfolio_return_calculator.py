import numpy as np

# asset a = 0.5(bobot), 0.3(return)
# asset b = 0.3(bobot), 0.1(return)
# asset c = 0.2(bobot), -0.9(return)

a_bobot = 0.5
a_return = 0.3
b_bobot = 0.3
b_return = 0.1
c_bobot = 0.2
c_return = -0.9

bobot = np.array([a_bobot, b_bobot, c_bobot])
return_asset = np.array([a_return, b_return, c_return])
if len(bobot) != len(return_asset):
    print("Informasi tidak sesuai")

bobot_sum = bobot.sum()
if bobot_sum != 1:
    print("Jumlah bobot tidak sesuai!")
else : 
    print("Total bobot: ", bobot.sum()*100, "%")

cont_a = a_return * a_bobot
cont_b = b_return * b_bobot
cont_c = c_return * c_bobot

total_port = bobot @ return_asset
print("Return portfolio: ", round(total_port, 20))
print("Return portfolio dalam persen: ", round(total_port*100, 20), "%")
print(f" Aset A: bobot {a_bobot}, return {a_return}, kontribusi {cont_a}")
print(f" Aset B: bobot {b_bobot}, return {b_return}, kontribusi {cont_b}")
print(f" Aset C: bobot {c_bobot}, return {c_return}, kontribusi {cont_c}")