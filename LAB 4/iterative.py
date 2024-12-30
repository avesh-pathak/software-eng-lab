import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For visualization

data = {1: 15, 2: 18, 3: 22, 4: 28, 5: 35} 
x = np.array(list(data.keys()))
y = np.array(list(data.values()))
coefficients = np.polyfit(x, y, 2) 
a, b, c = coefficients
predictions = [quadratic_model(a, b, c, day) for day in x]
errors = y - np.array(predictions)
print(f"Iteration 1 Errors: {errors}")


new_data = {6: 45, 7: 58}  # Extend dataset
x_new = np.array(list(new_data.keys()))
y_new = np.array(list(new_data.values()))
x_combined = np.append(x, x_new)
y_combined = np.append(y, y_new)
def quadratic_model(a, b, c, x):
    return a * x**2 + b * x + c
coefficients = np.polyfit(x_combined, y_combined, 2)  # Refit model
a, b, c = coefficients
predictions_combined = [quadratic_model(a, b, c, day) for day in x_combined]
errors_combined = y_combined - np.array(predictions_combined)
print(f"Iteration 2 Errors: {errors_combined}")


plt.plot(x_combined, y_combined, 'ro', label='Actual Data')
plt.plot(x_combined, predictions_combined, 'b-', label='Predicted Curve')
plt.legend()
plt.title("Iterative Methodology - Quadratic Model")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
