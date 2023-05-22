# introduction to python data types
    # - str
        # 'a', 'hello', "rahim", "I go to school"
        # """My name is Mainuddin. I
        # live in Barishal"""
        # a = str(1)
        # print(type(a))

        # print(type("Hello World"))

    # - int, float, complex
        # example of int: 1,10, 100, 33
        # example of float: 1.5, 10.3, 88.88333
        # example of complex: 10j, 77j

    # - list, tuple, range
        # info = ["rahim", 5, 3.9, [5, 6, "korim"]]
        # print(info[3][2])

        # info[3][2]

        # for i in info:
        #     print(i, type(i))

        #         # 0, 1, 2, 3
        # for i in range(10, 5, -2):

        # print(info[3][2])

        # print(info[3][2])

        # info1 = ("rahim", 5, 3.9, ["3", "korim", 9.9])

        # range(10) # here we've defined the ending position of a range
        # range(5, 10) # here we've defined starting position by giving 1st parameter and defined ending position by giving the 2nd parameter
        # range(1, 20, 2) # here the 1st parameter is the starting position, 2nd parameter is the ending position and the third parameter is the step

    # - dict
        # person = {"name": "Rahim", "age": 34, "height": 5.5, "number_of_childs": 2, "childs": [{"name": "Rafiq", "age": 13, "height": 4.5}, {"name": "Sofiq"}]}
        # person1 = ["Rahim", 34, 5.5]
        # print(person["name"], person["age"])
        # print(person["childs"][1]["name"])
        # person1 = ["Rahim", 15, "Male"]
        # person1[0]
        # person["age"] = 55

        # print(person["age"])
        # print(type(person))

    # - set, frozenset
# students = {"Rahim", "Karim", "Noman", "Hasib", "Rahim", "Rahim", "Noman"}
        # print(students)
        # print(students[0])
# print("Rahim" in students)
        # frozenset((1, 3, 5, 8, 8, 5))

    # - bool
            # students = [{"name": "Rahim", "age": 13, "gender": "Male"}, {"name": "Rahima", "age": 15, "gender": "Female"}]
            # True, False
            # is_male = True

    # - bytes, bytearray, memoryview

    # - None
    # number_of_packets = 5
    # number_of_packets = None
    # print(type(number_of_packets))

# operators in python
    # - Arithmetic operators
        # +, -, *, /, %, **, //

        # print(10 ** 3)

        # print(10 // 3)

        # PEMDAS
        # P = PARENTHESIS ()
        # E = EXPONENT **
        # M = MULTIPLICATION *
        # D = DIVISION /
        # A = ADDITION +
        # S = SUBTRACTION -
        # print((5 + (4 - 9)) / 2 * 6 - 1 + 3)

    # - Assignment operators
        # =, +=, -=, /=, %=, //=, **=

        # name = "Rahim"

        # age = 15

        # age = age + 3

        # age += 3

    # - Comparison operators
        # ==, !=, >, <, >=, <=
        # print(3 >= 3)

    # - Logical operators
        # and, or, not

        # rahims_age = 33
        # karims_age = 25
        # abduls_age = 15

        # if rahims_age > karims_age and rahims_age > abduls_age:
        #     print("Rahim is the elder brother")

        # new_comer = "mlss"

        # if new_comer == "teacher" or new_comer == "student":
        #     print("You're welcome")

        # if not(new_comer == "teacher" and new_comer == "student"):
        #     print("Sorry, you're not welcome")

    # - Identity operators
        # is, is not

    # print(3 is 3)

    # - Membership operators
        # in, not in

    # students = ["Rahim", "Karim", "Sajal"]

    # print("Abdul" not in students)
        
    # - Bitwise operators

# operator precendence in Python

# input
    # print("HELLO")
    # name = input("What's your name: ")
    # print("Hi " + name + ". How are you?")
    # age = int(input())
    # print(type(age))
    # print(type(name))

# output
    # print("HELLO","World","HI",sep=",")

    # print("Hi there \"hello\". \nwho are you?")
    # print("Hi there", end="-")
    # print("How are you")

# variables
    # sum_of_numbers = 3 + 4 + 6

    # 1name = wrong_way
    # ! @ # $ % ^ & *
    # _name = "Rahim"
    # first_name = "Chowdhury"
    # print = "Rahim" # wrong way
    # for = "Karim"

    # NaMe = "Rahim"
    # first_name = "Chowdhury"

    # sum_of_numbers = None

    #     # pascal case = StudentOneName

    #     # camel case = studentOneName

    #     # snake case = student_one_name # used for declaring variables

    # print(sum_of_numbers)

    # int age; # valid in c programming language
    # age # this variable declaration is not valid in python programming
    # age = None

# comments
    #I am a student
    #jksdfjdsklfjdsfkldsfjsdf
    # #name = "Rahim"

"""fsdjfksdjsdflksdjfsdlkjfsdflkjsdflkjsdjds
fsdjkfldjfslkjfdsjlkfsdjfksd
dfjsdklfjdsfkjsdfkjsd"""