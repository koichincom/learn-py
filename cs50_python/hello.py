# Ask user for their name
name = input("What's your name? ").strip().title()

# Split user's name into first and last name
first, last = name.split(" ")

# Print out the user's name (with a capital letter and with no leading/trailing spaces)
print(f"Hello, {name}")
print(f"Hello, {first}")
