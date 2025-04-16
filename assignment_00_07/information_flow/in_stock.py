inventory = {
    "pear": 1000,
    "apple": 500,
    "banana": 200,
    "orange": 0
}

def num_in_stock(fruit):
    """Returns the number of fruits in stock or 0 if not in stock."""
    return inventory.get(fruit, 0)

def main():
    fruit = input("Enter a fruit: ").lower()  
    stock_count = num_in_stock(fruit)
    if stock_count > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock_count}")
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
