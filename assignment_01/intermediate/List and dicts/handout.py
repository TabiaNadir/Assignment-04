def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range."


def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Changed '{old_value}' to '{new_value}'."
    else:
        return "Index out of range."


def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid range."
    return lst[start:end]


def game():
    my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Quit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))
            print("Updated list:", my_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))

        elif choice == '4':
            print("Thanks for playing!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    game()
