country = ["US", "Canada", "UK", "Taiwan", "Japan"]
for item in country:
    print("a" in item)

even_num = []
for i in range(1,11):
    if i %2 == 0:
        even_num.append(i)
print(even_num)

numbers = input("input a num: ")
print(len(numbers))

num = int(input("input a num: "))
digits = 0
while num > 0:
    num = num // 10
    digits += 1
print(digits)