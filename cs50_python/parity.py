# num = int(input("Number: "))
#
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

def main():
    x = int(input("Number: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    # Turn these 4 lines into 1 line

    # return True if n % 2 == 0 else False
    return n % 2 == 0

main()