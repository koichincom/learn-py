friends = ["Jim", "Karen", "Kevin"]

# for i in "Giraffe Academy":
#     print(i)

# for friends in friends:
#     print(friends)
#
# for index in range(1, 10):
#     print(index)

for index in range(len(friends)):
    print(friends[index])

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")