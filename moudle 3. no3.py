# Hemoglobin level checker

gender = input("Enter biological gender (male/female): ").lower()
hb = int(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hb < 117:
        print("Hemoglobin value is low.")
    elif hb <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")

elif gender == "male":
    if hb < 134:
        print("Hemoglobin value is low.")
    elif hb <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")

else:
    print("Invalid gender entered.")


