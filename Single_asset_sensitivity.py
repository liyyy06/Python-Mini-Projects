from numpy import diff, array

x = array([100, 120]) # BTC
y = array([500, 560]) # PORTFOLIO

delta_x = diff(x)
delta_y = diff(y)
slope = (delta_y / delta_x).item()
if delta_x > 0 and delta_y > 0:
    print(f"Setiap kenaikan harga BTC sebesar $1, berkaitan dengan kenaikan nilai portfolio sebesar ${slope}")
elif delta_x > 0 and delta_y < 0:
    print("Setiap kenaikan harga BTC sebesar $1, berkaitan dengan penurunan nilai portfolio sebesar ${slope}")
elif delta_x < 0 and delta_y > 0:
    print("Setiap penurunan harga BTC sebesar $1, berkaitan dengan kenaikan nilai portfolio sebesar ${slope}")
elif delta_x < 0 and delta_y < 0:
    print("Setiap penurunan harga BTC sebesar $1, berkaitan dengan penurunan nilai portfolio sebesar ${slope}")

def f(x):
    return x**2

x = 4
h = 0.1

forward_diff = (f(x+h) - f(x))/h
backward_diff = (f(x) - f(x-h))/h
central_diff = (f(x+h) - f(x-h))/(2*h)

print("Forward difference: ", round(forward_diff, 2))
print("Backward difference: ", round(backward_diff, 2))
print("Central difference: ", round(central_diff, 2))