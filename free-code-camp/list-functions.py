
# Basic list functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']

# A function to count the number of Jim
def how_many_jim():
    print(f"How many Jim are there now?: {friends.count("Jim")}")

# Append, extend, insert, remove, pop, clear
friends.extend(lucky_numbers)
print(f"append: {friends}")

friends.append("Jim")
print(f"extend: {friends}")

friends.insert(1, "Kelly")
print(f"insert: {friends}")

friends.remove("Jim")
print(f"remove: {friends}")

friends.pop()
print(f"pop: {friends}")

how_many_jim()

friends.clear()
print(f"clear: {friends}")