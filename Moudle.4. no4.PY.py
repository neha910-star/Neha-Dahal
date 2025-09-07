import random
# Computer picks a random number between 1 and 10
secret_number = random.randint(1, 10)

guessed = False
attempts = 0  # count guesses

while not guessed:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Correct! 🎉 You guessed the number in {attempts} attempts.")
        guessed = True




