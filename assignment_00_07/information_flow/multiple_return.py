def get_user_data():
    # Ask for user input
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")

    # Return the user data as a tuple
    return first_name, last_name, email

def main():
    # Call get_user_data() and store the returned tuple
    user_data = get_user_data()
    
    # Print the received user data
    print("Received the following user data:", user_data)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
