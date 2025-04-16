phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add entry")
    print("2. Look up number")
    print("3. View all entries")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"{name} added to the phonebook.")
    elif choice == "2":
        name = input("Enter name to look up: ")
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")
    elif choice == "3":
        if not phonebook:
            print("Phonebook is empty.")
        else:
            print("\nPhonebook Entries:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
