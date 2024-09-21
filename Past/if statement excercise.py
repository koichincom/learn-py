weight = int(input("weight: "))
typeofweight = input("(K) g or (L)bs")

if typeofweight.upper() == "K":
    print("Weight in Kg: "+str(weight*2.20462))
elif typeofweight.upper() == "L":
    print("Weight in Kg: "+str(weight*0.453592))