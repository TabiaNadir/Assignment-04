def main ():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to be divided: "))
    quotient = num1 // num2
    remainder = num1 % num2
    print (f"\n The result of this divided is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()    