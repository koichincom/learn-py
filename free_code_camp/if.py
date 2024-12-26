is_male = False
is_tall = True

if is_male or is_tall:
    print("You are male, tall, or both.")
else:
    print("You are neither male or tall.")

if is_male and is_tall:
    print("You are both male and tall.")
elif is_male and not is_tall:
    print("You are male but not tall.")
else:
    print("You are either not male or not tall.")