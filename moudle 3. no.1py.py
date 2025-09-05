# Zander size limit program

# Ask the user for the fish length
length = int(input("Enter the length of the zander (cm): "))

# Size limit
limit = 42

if length < limit:
    shortage = limit - length
    print(f"Release the fish back into the lake! It is {shortage} cm below the size limit.")
else:
    print("The fish meets the size limit. You can keep it.")
