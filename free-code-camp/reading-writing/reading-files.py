employee_file = open("employees.txt", "r")

# r is for read
# w is for write
# a is for append
# r+ is for read and write

print(employee_file.readable())

employee_file.close()