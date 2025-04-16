import random

def main():
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
    
        guess = int(input("Enter a new number: "))

    print(f"Congrats! The number was: {secret_number}")

if __name__ == "__main__":
    main()
