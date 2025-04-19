import random
import string

word_list = ['python', 'hangman', 'developer', 'streamlit', 'project']

secret_word = random.choice(word_list)
letters_in_word = set(secret_word) 
alphabet = set(string.ascii_lowercase)  
guessed_letters = set()

lives = 6

while len(letters_in_word) > 0 and lives > 0:
    print(f"\nYou have {lives} lives left.")
    print("Guessed letters:", ' '.join(sorted(guessed_letters)))

    word_display = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print("Current word:", ' '.join(word_display))

    user_letter = input("Guess a letter: ").lower()
    if user_letter in alphabet - guessed_letters:
        guessed_letters.add(user_letter)

        if user_letter in letters_in_word:
            letters_in_word.remove(user_letter)
            print("✅ Good guess!")
        else:
            lives -= 1
            print("❌ Wrong letter.")
    
    elif user_letter in guessed_letters:
        print("⚠️ You already guessed that letter.")
    else:
        print("❗ Invalid input. Please enter a letter.")
if lives == 0:
    print(f"\n💀 You died! The word was '{secret_word}'")
else:
    print(f"\n🎉 You guessed the word '{secret_word}' correctly!")

