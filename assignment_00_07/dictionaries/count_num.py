counts = {}
while True:
    user_input = input("Enter a number: ")
    if user_input.strip() == "":
        break
    number = int(user_input)
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1
for number, count in counts.items():
    print(f"{number} appears {count} times.")
