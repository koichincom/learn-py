employee_file = open("employees.txt", "r")

# r is for read
# w is for write
# a is for append
# r+ is for read and write

# print(employee_file.read())
# print(employee_file.readline()
print(employee_file.readlines())

employee_file.close()