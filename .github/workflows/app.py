def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("\n--- Temperature Converter ---")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius (Not implemented yet)")
    
    choice = input("Choose an option (1-2): ")
    if choice == '1':
        c = float(input("Enter temperature in Celsius: "))
        print(f"{c}°C is equal to {celsius_to_fahrenheit(c)}°F")
    else:
        print("Feature coming soon!")

if __name__ == "__main__":
    main()
