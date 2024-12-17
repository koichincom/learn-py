year = [1999,2020,2024,2027]

i = 1
newYear = 1999
while i < 4:
    year[i] = newYear+i
    i+=1

age = [8,17,5,40,2]
age.sort()
age.reverse()
print(sorted(age))

counter = [1,1,1,2,2,2,3,3,3]
print(counter.count(1))

duplicates = ["a", "b", "c","a", "b", "d","a", "c","b", "b"]
duplicates = set(duplicates)

print(duplicates)
