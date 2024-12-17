import copy

friends = [["Alice", "Bob"], ["Charlie"]]
friends2 = friends.copy()  # Shallow copy
friends3 = copy.deepcopy(friends)  # Deep copy

friends2[0].append("David")  # Modify the inner list
print("friends:", friends)    # [['Alice', 'Bob', 'David'], ['Charlie']]
print("friends2:", friends2)  # [['Alice', 'Bob', 'David'], ['Charlie']]
print("friends3:", friends3)  # [['Alice', 'Bob'], ['Charlie']] (unaffected)