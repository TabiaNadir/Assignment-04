def get_last_element(lst):
    """
    Prints the last element in the given non-empty list.
    """
    print("last element:", lst[-1])

def main():
    num_elements = int(input("How many elements do you want to enter? ")) 
    user_list = []
    for i in range(num_elements):
        item = input(f"Enter element #{i + 1}: ")
        user_list.append(item)
    get_last_element(user_list)

if __name__ == '__main__':
    main()
