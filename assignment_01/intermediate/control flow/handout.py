import random

NUM_ROUNDS = 5

def get_user_choice():
    while True:
        choice = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if choice in ["higher", "lower"]:
            return choice
        else:
            print("Please enter either higher or lower.")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        player_num = random.randint(1, 100)
        computer_num = random.randint(1, 100)

        print(f"Your number is {player_num}")
        choice = get_user_choice()

        correct = False
        if choice == "higher" and player_num > computer_num:
            correct = True
        elif choice == "lower" and player_num < computer_num:
            correct = True

        if correct:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {score}\n")

    print("Thanks for playing!")

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
