
def engineering_calculator():
    print("=== Engineering Calculator ===")
    print("1. Calculate Voltage")
    print("2. Calculate Current")
    print("3. Calculate Resistance")
    print("4. Calculate Power")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        current = float(input("Enter current (A): "))
        resistance = float(input("Enter resistance (ohms): "))
        print("Voltage =", current * resistance, "V")

    elif choice == "2":
        voltage = float(input("Enter voltage (V): "))
        resistance = float(input("Enter resistance (ohms): "))
        if resistance == 0:
            print("Resistance cannot be zero.")
        else:
            print("Current =", voltage / resistance, "A")

    elif choice == "3":
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        if current == 0:
            print("Current cannot be zero.")
        else:
            print("Resistance =", voltage / current, "ohms")

    elif choice == "4":
        voltage = float(input("Enter voltage (V): "))
        current = float(input("Enter current (A): "))
        print("Power =", voltage * current, "W")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    engineering_calculator()
