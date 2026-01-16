# Simple Electrical Load & Ohm's Law Calculator
def calculate_ohm():
    print("--- Ohm's Law Calculator ---")
    v = float(input("Enter Voltage (V): "))
    r = float(input("Enter Resistance (R): "))
    i = v / r
    p = v * i
    print(f"Current (I): {i} Amps")
    print(f"Power (P): {p} Watts")

calculate_ohm()
