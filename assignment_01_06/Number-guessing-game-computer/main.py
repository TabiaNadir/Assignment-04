import random

def computer_guess_game():
    low = 1
    high = 100
    feedback = ''
    guess_count = 0

    print("Think of a number between 1 and 100, and I (the computer) will try to guess it!")
    print("After each guess, type: 'high', 'low', or 'correct'.")

    while feedback != 'correct':
        if low > high:
            print("Hmm... something went wrong with your hints 😅")
            break

        guess = random.randint(low, high)
        guess_count += 1
        print(f"\n🤖 My guess is: {guess}")
        feedback = input("Your feedback (high / low / correct): ").lower()

        if feedback == 'high':
            high = guess - 1
        elif feedback == 'low':
            low = guess + 1
        elif feedback == 'correct':
            print(f"\n🎉 Yay! I guessed your number {guess} in {guess_count} tries!")
        else:
            print("Please type 'high', 'low', or 'correct'.")

# Start the game
computer_guess_game()

