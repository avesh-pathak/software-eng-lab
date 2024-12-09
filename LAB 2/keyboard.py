def calculate_w(t, h):
    return (0.5 * t**2 - 0.2 * h - 15) / 0.9

def main():
    print("\nUsing the formula:")
    print("w = (0.5 * t^2 - 0.2 * h - 15) / 0.9")
    
    while True:
        try:
            temperature = float(input("Enter temperature in °C: "))
            humidity = float(input("Enter humidity in %: "))
            if 0 <= humidity <= 100:
                break
            else:
                print("Humidity must be between 0% and 100%.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    w = calculate_w(temperature, humidity)
    print(f"\nFor Temperature: {temperature}°C and Humidity: {humidity}%")
    print(f"Calculated w: {w}")

if __name__ == "__main__":
    main()
