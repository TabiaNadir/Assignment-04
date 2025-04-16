def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. 
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    return False

def main():
    # Test cases to demonstrate the function's behavior
    print(in_range(5, 1, 10))  # True, because 5 is between 1 and 10
    print(in_range(1, 1, 10))  # True, because 1 is equal to the low bound
    print(in_range(10, 1, 10))  # True, because 10 is equal to the high bound
    print(in_range(0, 1, 10))  # False, because 0 is less than the low bound
    print(in_range(11, 1, 10))  # False, because 11 is greater than the high bound

if __name__ == '__main__':
    main()

