name = input("Enter a name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")

story = f"""
One day, {name} went to {place} and saw a {adjective} {animal}.
Without thinking, {name} decided to {verb} with it.
It was the start of a very strange adventure!
"""

print("\nHere's your Mad Libs story:")
print(story)
