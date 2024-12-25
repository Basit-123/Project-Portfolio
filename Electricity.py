def main():
    # Initial states
    electricity = False  # Electricity is initially off
    ups = not electricity  # UPS is on when electricity is off

    # Display initial states
    print(f"Electricity: {'On' if electricity else 'Off'}")
    print(f"UPS: {'On' if ups else 'Off'}")

    # Toggle Electricity state
    electricity = not electricity  # Change the electricity state (simulate ON)
    ups = not electricity  # UPS state depends on electricity

    print("\nAfter toggling electricity:")
    print(f"Electricity: {'On' if electricity else 'Off'}")
    print(f"UPS: {'On' if ups else 'Off'}")



if __name__ == "__main__":
    main()
