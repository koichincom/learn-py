customer = {
    "name":"Koichi Nakayamada",
    "age":20,
    "gender":"male"
}

customer["age"] = 30
print(customer["age"])

customer["grade"] = "A+"

print(customer)


phone = input("What's your phone number?: ")
numbers = {
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    0:"zero"
}
 
for num in phone:
    num = int(num)
    print(numbers[num], end=", ")

check = input("What's your vision?: ")
numbers = {
    1:"one",
    2:"two",
    3:"three",
    4:"now",
    5:"five",
    6:"tokyo",
    7:"seven",
    8:"eight",
    9:"stop",
    0:"Don't"
}
 
for num in phone:
    num = int(num)
    print(numbers[num], end=", ")