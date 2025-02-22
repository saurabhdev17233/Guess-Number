import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have a number(1-100). Try to guess it!")
#github:saurabhdev17233
while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} correctly! 🎉")
            break
    except ValueError:
        print("Please enter a valid number.")
