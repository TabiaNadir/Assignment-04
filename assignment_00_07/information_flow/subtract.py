def subtract_seven(num):
    """Subtracts 7 from the given number and returns the result."""
    return num - 7

def main():
    num = int(input("Enter a number: "))
    result = subtract_seven(num)
    print("The result after subtracting 7 is:", result)

if __name__ == '__main__':
    main()
