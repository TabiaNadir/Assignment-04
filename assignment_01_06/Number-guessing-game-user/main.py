import random

def user_guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("Too low! Try a higher number.\n")
            elif user_guess > number_to_guess:
                print("Too high! Try a lower number.\n")
            else:
                print(f"🎉 Correct! You guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print("❗ Please enter a valid number.\n")

# Run the game
user_guess_game()
