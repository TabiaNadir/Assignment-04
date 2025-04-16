def main():
    affirmation = "I am capable of doing anything I put my mind to."
    
    print(f"Please type the following affirmation: {affirmation}")
    user_input = input()

    while user_input != affirmation:
        print("Hmmm That was not the affirmation.")
        print(f"Please type the following affirmation: {affirmation}")
        user_input = input()
    
    print("That's right! :)")

if __name__ == '__main__':
    main()
