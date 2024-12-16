
def calculate_weather_index(t, h):
    
    return (0.5 * t**2 - 0.2 * h - 15) / 0.9


def multiple_inputs_file_solution(filename):
    try:
        with open(filename, 'r') as file:
            print("\nMultiple Inputs from File:")
            for i, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue
                t, h = map(float, line.split())
                w = calculate_weather_index(t, h)
                print(f"Temperature: {t}, Humidity: {h}, Weather Index: {w:.2f}")
    except Exception as e:
        print(f"Error reading the file: {e}")


filename = r'C:\Users\iamav\Desktop\Sem 6\Software Eng Lab\LAB 2\multiple_inputs_weather.txt'
multiple_inputs_file_solution(filename)
