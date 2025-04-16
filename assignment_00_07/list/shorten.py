MAX_LENGTH = 3

def shorten(lst):
    """
    Removes and prints items from the end of lst until it's MAX_LENGTH items long.
    Leaves the list unchanged if it's already short enough.
    """
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  
        print("Removed:", removed)

def main():
    items = []
    while True:
        val = input("Enter an item (press Enter to stop): ")
        if val == "":
            break
        items.append(val)
    
    print("\nOriginal list:", items)
    shorten(items)
    print("Shortened list:", items)

if __name__ == '__main__':
    main()
