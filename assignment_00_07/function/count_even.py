def count_even(lst):
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(f"Number of even numbers: {even_count}")

def main():
    user_list = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        else:
            try:
                user_list.append(int(user_input))
            except ValueError:
                print("Please enter a valid integer.")
    
    count_even(user_list)

if __name__ == '__main__':
    main()
