def main():
    C = 299_792_458

    mass = float(input("Enter kilos of mass: "))
    print ("\ne = m * C^2...\n")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s\n")
    energy = mass * C**2
    print(f"{energy} joules of energy!")

if __name__ == "__main__":
    main()    