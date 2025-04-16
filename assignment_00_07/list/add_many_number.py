from typing import Union

def add_many_number(numbers: list[Union[int,float]]) -> float:
    """ take in a list of number (ints and/or floats) and 
        return the sum of those numbers."""
    total_so_far: float = 0.0
    for number in numbers:
        total_so_far += number
    return total_so_far

def main():
    numbers: list[Union[int, float]] = [1, 2.5, 3, 4.75]
    sum_of_numbers: float = add_many_number(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()