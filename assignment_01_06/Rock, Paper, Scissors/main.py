import random

def play_rps():
    options = ['rock', 'paper', 'scissors']
    computer = random.choice(options)
    
    user = input("Choose rock, paper, or scissors: ").lower()

    if user not in options:
        print("❗ Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"\n🧑 You chose: {user}")
    print(f"💻 Computer chose: {computer}")

    if user == computer:
        print("🤝 It's a tie!")
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        print("✅ You win!")
    else:
        print("❌ You lose.")
while True:
    play_rps()
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Thanks for playing!")
        break
