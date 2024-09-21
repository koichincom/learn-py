array = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"]
 ]

array[2][1] = "x"
print(array)

for row in array:
    for value in row:
        print(value)

