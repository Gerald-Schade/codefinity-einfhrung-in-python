prices = [29.99, 45.50, 12.75, 38.20]

for i in range(len(prices)):
    if i  == 0:
        prices[0] *= 0.9
    elif i == 1:
        prices[1] *= 0.8
    elif i == 2:
        prices[2] *= 0.85
    elif i == 3:
        prices[3] *= 0.95
    print(f"Updated price for item {i}: ${prices[i]:.2f}")






