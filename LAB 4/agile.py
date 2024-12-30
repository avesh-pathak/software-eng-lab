import numpy as np  # For numerical computations
import matplotlib.pyplot as plt  # For visualization
def quadratic_model(a, b, c, x):
    return a * x**2 + b * x + c
data = {1: 15, 2: 18, 3: 22, 4: 28, 5: 35}
x = np.array(list(data.keys()))
y = np.array(list(data.values()))
coefficients = np.polyfit(x, y, 2)
a, b, c = coefficients

# Sprint 2: Visualization
predictions = [quadratic_model(a, b, c, day) for day in x]
plt.plot(x, y, 'ro', label='Actual Data')
plt.plot(x, predictions, 'b-', label='Predicted Curve')
plt.legend()
plt.title("Agile Sprint 2 - Visualization")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()

# Sprint 3: Error analysis
errors = y - np.array(predictions)
print(f"Sprint 3 Errors: {errors}")

# Sprint 4: Real-time data integration (Simulated API fetch)
def fetch_real_time_data():
    # Simulating fetching data (in practice, use APIs like OpenWeather)
    return {6: 45, 7: 58}

real_time_data = fetch_real_time_data()
x_rt = np.array(list(real_time_data.keys()))
y_rt = np.array(list(real_time_data.values()))
x_combined = np.append(x, x_rt)
y_combined = np.append(y, y_rt)

coefficients = np.polyfit(x_combined, y_combined, 2)  # Refit with new data
a, b, c = coefficients
predictions_combined = [quadratic_model(a, b, c, day) for day in x_combined]

# Final visualization
plt.plot(x_combined, y_combined, 'ro', label='Actual Data (Extended)')
plt.plot(x_combined, predictions_combined, 'b-', label='Predicted Curve (Extended)')
plt.legend()
plt.title("Agile Sprint 4 - Real-Time Integration")
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.show()
