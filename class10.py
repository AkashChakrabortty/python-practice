# # print("three" + "four")

# # print(4 + 5.5)

# print(4 + "five")


# while True:
#     try:
#         number = int(input("Enter number to be trippled: "))
#         if number:
#             print(number * 3)
#             break
#         # else:
#         #     # print("Please enter a number greater than 0")
#         #     raise ValueError("Please enter something greater than 0")
#     except ValueError as error:
#         # print("Please enter a number")
#         print(error)
#     else:
#         print("You've some error")
#     # except:
#     #     print("You've entered wrong value")

# # print(type(number))

# print("Hello")



# SyntaxError = syntactical errors
# NameError = when a variable is not defined but we're try to use it
# TypeError = occurs when data type mismatch (like if we want to sum "two" + 5) or len(5)
# IndexError = when we try to acces a value with a invalid index (a = [1,2,3]  a[5])
# ValueError = when we try to call a built in function with a invalid agrument (int("ten"))
# KeyError = when we try to access a key that doesn't exist on the dictionary
# AttributeError = when we try to access attribute that doesn't exist ("hello".ugv)

# if we want to raise an exception without defining any error type we can simply do raise Exception

# def get(dictionary, key):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return None

# def add_students(class_name, *students_name):
#     class_names = ("one", "two", "three")
#     if class_name not in class_names:
#         raise ValueError("Class name must be one of 'one', 'two' or 'three'")


# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# You can use the else keyword to define a block of code to be executed if no errors were raised:

# The finally block lets you execute code, regardless of the result of the try- and except blocks.


# import pdb; pdb.set_trace()
# l = list all code
# n = execute next line
# p = print something (example p variable_name)
# c = continue



# with open('.ugv.txt', 'w') as file:
#     file.write("hello")

# try:
#     name
# except:
#     print("Something went wrong")

# print("hello")

# name

# number = 10

# try:
#     number + 5
# except:
#     print("Something went wrong")

# try:
#     number + 5
# # except NameError:
# #     name = "hello"
# #     print()
# # except TypeError:
# #     number = int(number) + 5
# #     print()
# except:
#     print("Something went wrong")

# number = '10'

# try:
#     number = number + 5
# except NameError:
#     name = "hello"
#     print()
# except TypeError:
#     number = int(number) + 5
# else:
#     print("everything is ok")
# finally:
#     print("Finally we did it")

# print(number)



from unicodedata import name


person = {"name": "Raihan"}

# print(person["age"])

# print(person.get("age"))

# def get(dictionary, key):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return None

# print(get(person, "age"))


class_one_students = []
class_two_students = []
class_three_students = []

classes = {
    "one": [],
    "two": [],
    "three": []
}

def add_students(class_name, *students): # 'one', 'two', 'three'   
    # print(class_name, students)
    try:
        for student in students:
            classes[class_name].append(student)
    except KeyError:
        print("Class name should be one of 'one', 'two', 'three'")

# print("class 1: ", classes["one"])
# print("class 2: ", classes["two"])
# print("class 3: ", classes["three"])

# add_students("two", "raihan", "saiful", "noman")

# print("class 1: ", classes["one"])
# print("class 2: ", classes["two"])
# print("class 3: ", classes["three"])

# try:
#     car
# except NameError as error:
#     print(error)




# print(class_name)

students = []

# print(students[3])

# print('10' + 5)

# students.add_koro()

# print("hello")


# try:
#     print(class_name)
# except NameError:
#     class_name = "rohim"
#     print(class_name)
#     # print("Variable not found")

# print("Hello")

# len(5)

# def len_checker(collection):
#     try:
#         print(f"Length of the collection is {len(collection)}")
#     except TypeError:
#         print("Please enter a collection of data not a singular data type")

# len_checker("hello")


# def sum_two_values(number1, number2):
#     try:
#         print(number1 + number2)
#     except TypeError:
#         print("Please enter a number")
#     except ValueError:
#         print("Please enter a valid input")
#     else:
#         print("Everything is fine")
#     finally:
#         print("Pogram execution done")

# sum_two_values(3, 10)

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("Please enter something greater than 0")
# except TypeError:
#     print("Please enter number")
# except:
#     print("You've entered something wrong")


person = {"name": "Rahat"}

# print(person["age"])

# print(person.get("age"))

# def get(dictionary, key):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return None

# print(get(person, "name"))

classes = {
    "one": [],
    "two": [],
    "three": []
}

# def add_students(class_name, *students): # 'one', 'two', 'three'
#     # print(class_name, students)
#     try:
#         for student in students:
#             # import pdb; pdb.set_trace() # pdb commands l = list_code, n = next_line, p = print, c = continue
#             if type(student) is not str:
#                 raise TypeError("Please enter a string as a student name")
#             classes[class_name].append(student)
#     except KeyError:
#         print("Please enter either 'one', 'two' or 'three' as class name")


# print("Class 1: ", classes["one"])
# print("Class 2: ", classes["two"])
# print("Class 3: ", classes["three"])

# add_students("two", "usha", "asha", "batasha", "pasha")

# add_students("eight", "robin", "sofiq")

# add_students("three", 3, 5)

# print("Class 1: ", classes["one"])
# print("Class 2: ", classes["two"])
# print("Class 3: ", classes["three"])




# print(student_name)

# print(3 + int("9"))

# print("Hello UGV")

# numbers = [1, 2, 3]
# numbers.ugv_method()

# def hello:
#     print("Hi")

# try:
#     # student_name
#     3 + '5'
#     # 3 + 5
# except TypeError:
#     print("Invalid data type")
# except NameError:
#     print("Variable not found")
# except ValueError:
#     print("Please enter a valid data")
# else:
#     print("No error found")
# finally:
#     print("Done")


person = {"name": "Sahin"}

# print(person["age"])

# print(person.get("age"))

# def get(dictionary, key):
#     try:
#         return dictionary[key]
#     except KeyError:
#         return None

# print(get(person, "name"))


# classes = {
#     "one": [],
#     "two": [],
#     "three": []
# }

# def add_students(class_name, *students): # "one", "two", "three"
#     # print(class_name, students)
#     if len(students) == 0:
#         raise ValueError("Please enter some student name")
#     try:
#         for student in students:
#             classes[class_name].append(student)
#     except KeyError:
#         print("Please enter either 'one', 'two' or 'three' as class name")

# # print("student 1: ", classes["one"])
# print("student 2: ", classes["two"])
# print("student 3: ", classes["three"])

# add_students("two", "rafiq", "sofiq", "jobbar")
# add_students("three","raihan", "jehad")

# try:
#     add_students("five")
# except ValueError:
#     print("Ooops! something went wrong")
#     add_students("three", "sohel", "arman")

# print("student 1: ", classes["one"])
# print("student 2: ", classes["two"])
# print("student 3: ", classes["three"])

name = "rohan"
age = 56
import pdb; pdb.set_trace() # l = show_block_of_code, n = execute_next_line, p = print, c = continue_excution_without_debugging, q = quit_debugging
products = ["shirt", "pant", "fruits"]
print("Execution done")
