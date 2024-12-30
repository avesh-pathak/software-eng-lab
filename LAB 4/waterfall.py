import numpy as np
import matplotlib.pyplot as plt


data = {1: 15, 2: 18, 3: 22, 4: 28, 5: 35}  


def quadratic_model(a, b, c, x):
    return a * x**2 + b * x + c


x = np.array(list(data.keys()))
y = np.array(list(data.values()))
coefficients = np.polyfit(x, y, 2)  
a, b, c = coefficients


predictions = [quadratic_model(a, b, c, day) for day in x]
print(f"Actual: {y}, Predicted: {predictions}")


plt.plot(x, y, 'ro', label='Actual Data')
plt.plot(x, predictions, 'b-', label='Predicted Curve')
plt.legend()
plt.title("Waterfall Methodology - Quadratic Model")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
