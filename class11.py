# file = open("hello.txt", 'r')

# print(file.read())
# print(file.read())
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())
# text_lines = file.readlines()
# print(text_lines)


# file = open("hello.txt", 'w')

# file.write("Hello again 2nd time")

# file = open("hello.txt", "a")

# file.write("\nHi there")

# file = open("hello.txt", 'w')

# file = open("hello.txt", 'x') # gives error if file already exists

# file = open("hi.txt", "a")

# file = open("hello.txt", 'r')

# print(file.readline())
# print(file.readline())
# file.seek(1)
# print(file.readline())
# print(file.readline())

# file = open("hello.txt", "r+")

# print(file.readline())
# file.seek(0)
# file.write("\nWe're learning python\n")

# list_of_students = ["Rahim", "Karim", "Sohan", "Noman", "Ashiq", "Tripti"]

# file = open("student_list.txt", 'a')

# for student in list_of_students:
#     # file.write(student + "\n")
#     file.write(f"{student}\n")



# file = open("hi.txt", 'r')

# print(file.read())
# file.seek(0)
# print(file.read())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.seek(0)
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# file = open("hello.txt", 'w')

# file.write("We're writing something\n")
# file.write("Whats the problem")

# file = open("hello.txt", "a")

# file.write("\nWe're writing again")

# file = open("simple_file.txt", "x")

# file.close()

# with open("student_list.txt", 'r') as file:
#     print(file.read())

# print("hello")


# with open("hi.txt", "r+") as file:
#     print(file.read())
#     file.write("Hi there")
#     # print(file.read())


# student_list = []

# with open("student_list.txt", "r") as file:
#     # for student in file.readlines():
#     #     # print(type(student))
#     #     # print(student[:-1])
#     #     # print(student.replace("\n", ""))
#     #     student_list.append(student.replace("\n", ""))

#     student_list = [student.replace("\n", "") for student in file.readlines()]

# print(student_list)











# file = open("hello.txt", "r")

# print(file.read())
# print(file.read())
# print(file.readline(2))
# print(file.readlines()[1])
# print(file.read().split("\n")[1])
# file.close()

# file = open("batch_4_1.txt", "w")

# file.write("Hello from UGV\n")
# file.write("We're learning python")
# file.writelines(["\nWe're doing great", "\nWe hope the best"])


# file = open("batch_4_1.txt", "a")

# file.write("\nWe're writing again")

# file = open("batch_4_1.txt", "r")

# print(file.read())
# file.seek(5)
# print(file.read())

# file = open("batch_4_1.txt", "r+")

# # print(file.read())
# file.seek(0)
# file.write("We're editing again with read/write mode")
# print(file.closed)
# file.close()
# print(file.closed)

# with open("batch_4_1.txt", "r") as file:
#     print(file.read())

# print(file.readline())

students_list = []

with open("student_list.txt", "r") as students:
    # print(students.read())
    splitted_students = students.read().split("\n")
    # for student in splitted_students:
    #     students_list.append(student.upper())

    students_list = [student.upper() for student in splitted_students]

print(students_list)

