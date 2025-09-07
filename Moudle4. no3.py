# Program to find the smallest and largest numbers

numbers = []  # empty list to store user inputs

while True:
    user_input = input("Enter a number (empty to quit): ")

    if user_input == "":  # stop if user enters empty string
        break

    number = float(user_input)  # convert to number
    numbers.append(number)

if numbers:  # check if the list is not empty
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
