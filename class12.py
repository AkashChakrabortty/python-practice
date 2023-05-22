# class_name_one #snake case (used for naming variables and function)
# classNameOne #camel case
# ClassNameOne #pascal case (used for naming classes)

# class Student:
#     name = "Sohan"
#     age = 45

#     def do_math(self):
#         return 3 + 5

# student1 = Student()
# student2 = Student()

# print(student1.name)
# print(student1.age)

# print(student2.name)
# print(student2.age)

# print(student1 is student2)

# class Student:
#     def __init__(self, name, age, cgpa):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         # print("Hello again")

#     def __del__(self):
#         print("Destructor called")

#     def print_my_name(self):
#         print(f"My name is {self.name}")

# student1 = Student("Akash", 25, 3.1)
# student2 = Student("Opey", 32, 1.3)

# student1.print_my_name()

# print(f"student1 name is {student1.name}. student1 age is {student1.age}. student1 cgpa is {student1.cgpa}")









# def function_name():
#     pass

# class Student:
#     def __init__(self, name, age, cgpa, roll):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         self.roll = roll

#     def participate_exam(self):
#         print(f"{self.name} participated the exam")

#     def increment_birth_year(self, age_to_be_incremented):
#         self.age = self.age + age_to_be_incremented
#         # self.age += 1


# student1 = Student("Akash", 22, 3.8, 24)
# student2 = Student("Azmal Gazi", 30, 4, 32)

# print(student1.name)
# print(student1.age)
# student1.participate_exam()
# student1.increment_birth_year(10)
# print(student1.age)

# print(student2.name)
# print(student2.cgpa)
# student2.participate_exam()






# def function_name():
#     pass

# function_name()

# class Student:
#     pass

# ClassName()

class Student:
    def __init__(self, name, age, cgpa, roll): # constructor
        # print(name, age, cgpa, roll, sep=" ")
        self.name = name
        self.age = age
        self.cgpa = cgpa
        self.roll = roll
        self._hand_cash = 5000
        # print("Hello from the object")

    # def increment_age(self):
    #     self.age = self.age + 1

    def increment_age(self, age_to_be_increment):
        self.age = self.age + age_to_be_increment

    # private hand_cash = 5000

    def purchase_something(self, amount):
        self._hand_cash = self._hand_cash - amount
        return f"Now you've only {self._hand_cash} taka"

    def __del__(self):
        print("Desctructor called")


student1 = Student("Antareep", 25, 3.8, 15)
student2 = Student("Sadia", 45, 4, 1201147)
print(student1)
print(student1.name)
print(student1.age)
student1.increment_age(40)
print(student1.age)
print(student1.purchase_something(300))
# print(student1._hand_cash) # don't do this

# print(student2.name)
# print(student2.age)
# student2.increment_age(1)
# print(student2.age)

# student2 = Student()

# print(student1.name, student1.age)
# print(student2.name, student2.age)

# # print(student1 == student2)
# print(student1 is student2)





# def function_name():
#     return "something"

# variable1 = function_name()

# class ClassName:
#     pass

# classObject = ClassName()

# class Student:
#     name = "Aksah"
#     age = 25
#     cgpa = 3.8
#     roll = 12

# class Student:
#     def __init__(self, name, age, cgpa, roll):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         self.roll = roll
#         self._pocket_money = 5000

#     def print_my_name(self):
#         print(f"My name is {self.name}")

#     def increment_my_age(self, age_to_be_incremented):
#         self.age = self.age + age_to_be_incremented

#     # private string variable_name = "dfdsfsd"

#     def purchase_something(self, amount):
#         self._pocket_money = self._pocket_money - amount
#         return self._pocket_money


#     def check_pocket_money(self):
#         return self._pocket_money


#     def __del__(self):
#         print("destructor called")

# student1 = Student("Sazzat", 25, 3.7, 13)

# print(student1.name)
# print(student1.age)
# print(student1.purchase_something(200))

# print(student1.purchase_something(500))

# student1.print_my_name()

# student1.increment_my_age(2)

# print(student1.check_pocket_money())

# print(student1.age)

# student2 = Student("Aminul", 30, 3.5, 15)

# print(student2.name)
# print(student2.age)

# student2.print_my_name()

# student2.increment_my_age(3)
# print(student2.age)

# print(student1 == student2)
# print(student1 is student2)


# class Student:

#     def __init__(self, name, age, cgpa, roll):
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         self.roll = roll
#         self._pocket_money = 5000

#     def __del__(self):
#         print("Destructor called")

#     def buy_something(self, amount):
#         self._pocket_money = self._pocket_money - amount
#         return self._pocket_money


    
        

# student1 = Student("Sahed", 23, 4, 34)
# student2 = Student("Sohan", 23, 4, 34)

# print(student1)

# print(student1.name)
# print(student2.name)

# print(student1._pocket_money)

# print(student1.buy_something(100))

# # print(student1.age)






