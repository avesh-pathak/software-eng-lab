def calculate_w(t, h):
    return (0.5 * t**2 - 0.2 * h - 15) / 0.9

def main():
    print("\nUsing the formula:")
    print("w = (0.5 * t^2 - 0.2 * h - 15) / 0.9")
    print("\nEnter the temperature and humidity:")
    temperature = 20  
    humidity = 60     
    
    w = calculate_w(temperature, humidity)
    print(f"\nFor Temperature: {temperature}°C and Humidity: {humidity}%")
    print(f"Calculated w: {w}")

if __name__ == "__main__":
    main()
