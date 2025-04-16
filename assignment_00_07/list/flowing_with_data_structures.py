def add_three_copies(target_list: list, data):
    """
    Adds three copies of the given data to the target_list.
    This modifies the list in place — no return needed.
    """
    for _ in range(3):
        target_list.append(data)

def main():
    message = input("Enter a message to copy: ")
    messages = []
    print("\nList before:", messages)
    add_three_copies(messages, message)
    print("List after:", messages)

if __name__ == '__main__':
    main()
