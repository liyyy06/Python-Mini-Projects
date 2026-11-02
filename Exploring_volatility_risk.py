import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
mu = 1.08 ** (1/252) - 1 #8%
days = 252 * 10 #10 tahun

A = rng.normal (mu, 0.0025, days)
B = rng.normal (mu, 0.02, days)

vol_A_harian = A.std()
vol_B_harian = B.std()

vol_A_tahunan = vol_A_harian * np.sqrt(252)
vol_B_tahunan = vol_B_harian * np.sqrt(252)

print (vol_A_tahunan)
print (vol_B_tahunan)

ret_A = A.mean() * 252
ret_B = B.mean() * 252
print(round(ret_A, 3), round(ret_B, 3))

for s in (0.0025, 0.02) : 
    r = rng.normal(mu, s, (100000, 252))
    print (((1+r).prod(1)<1).mean())

plt.plot(A[:252], label="A")
plt.plot(B[:252], label="B")
plt.title('Return Harian')
plt.legend()
plt.show()
