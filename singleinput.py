def calculate_weather_index(t, h):
    return (0.5 * t**2 - 0.2 * h - 15) / 0.9

filename = 'C:/Users/iamav/Desktop/Sem 6/Software Eng Lab/LAB 2/single_input_weather.txt'

try:
    with open(filename, 'r') as file:
        line = file.readline().strip()
        t, h = map(float, line.split())
        w = calculate_weather_index(t, h)
        print("\nUsing the formula:")
        print("w = (0.5 * t^2 - 0.2 * h - 15) / 0.9")
        print(f"File input -> Temperature: {t}, Humidity: {h}, Weather Index: {w:.2f}")
except Exception as e:
    print(f"Error reading the file: {e}")
