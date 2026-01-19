import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("🎯 Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print(f"You have {max_attempts} attempts to guess it.\n")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.\n")
        elif guess > secret_number:
            print("📈 Too high! Try again.\n")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("❌ Please enter a valid number.\n")

if attempts == max_attempts and guess != secret_number:
    print(f"😢 Game Over! The correct number was {secret_number}.")
