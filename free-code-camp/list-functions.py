
# Basic list functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ['Kevin', 'Karen', 'Jim', 'Oscar', 'Toby']

# A function to count the number of Jim
def how_many_jim():
    print(f"How many Jim are there now?: {friends.count("Jim")}")

# Testing copy function
friends1 = friends
print(f"equal: {friends1}")

friends2 = friends.copy()
print(f"copy: {friends2}")

"""# Append, extend, insert, remove, pop, clear

friends.sort()
print(f"sort: {friends}")

friends.extend(lucky_numbers)
print(f"append: {friends}")

friends.append("Jim")
print(f"extend: {friends}")

friends.insert(1, "Kelly")
print(f"insert: {friends}")

print(f"count: {friends.count("Jim")}")

lucky_numbers.reverse()
print(f"reverse: {lucky_numbers}")

friends.remove("Jim")
print(f"remove: {friends}")

friends.pop()
print(f"pop: {friends}")

how_many_jim()

friends.clear()
print(f"clear: {friends}")"""