def get_first_element(lst):
    """
    Prints the first element in the given non-empty list.
    """
    print("First element:", lst[0])

def main():
    num_elements = int(input("How many elements do you want to enter? "))
    user_list = []
    for i in range(num_elements):
        item = input(f"Enter element #{i + 1}: ")
        user_list.append(item)  
    get_first_element(user_list)

if __name__ == '__main__':
    main()
