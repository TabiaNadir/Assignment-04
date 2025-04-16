minimum_height = 50
while True:
    user_input = input("How tall are you? ")
    if user_input.strip() == "":
        print("Thanks for checking! Have a great day!")
        break
    try:
        height = int(user_input)
        if height >= minimum_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
    except ValueError:
        print("Please enter a valid number or press Enter to exit.")
