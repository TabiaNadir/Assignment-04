GRAVITY_FACTORS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").capitalize()
    if planet in GRAVITY_FACTORS:
        gravity = GRAVITY_FACTORS[planet]
        planetary_weight = round(earth_weight * gravity, 2)
        print(f"The equivalent weight on {planet}: {planetary_weight}")
    else:
        print("Unknown planet. Please enter a valid planet name (e.g., Mars, Jupiter).")

if __name__ == "__main__":
    main()
