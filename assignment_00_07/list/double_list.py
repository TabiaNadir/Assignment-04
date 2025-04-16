def double_number(numbers: list[int]) -> list[int]:
    """Take a list of integer and return a new list with 
       each elemant doubled"""
    doubled = [number * 2 for number in numbers]
    return doubled

def main():
    numbers: list[int] = [1, 2, 3, 4]
    print (double_number(numbers))

if __name__ == "__main__":
    main()