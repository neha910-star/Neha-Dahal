# Inches to centimeters converter

while True:
    inches = float(input("Enter length in inches (negative to quit): "))

    if inches < 0:   # stop when user enters negative
        print("Program ended.")
        break

    centimeters = inches * 2.54
    print(f"{inches} inches = {centimeters:.2f} cm")
