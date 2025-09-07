# Correct credentials
correct_username = "python"
correct_password = "rules"

# Maximum number of attempts
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")
    attempts += 1

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break
    else:
        print("Incorrect username or password. Try again.")

if attempts == max_attempts and (username != correct_username or password != correct_password):
    print("Access denied.")
