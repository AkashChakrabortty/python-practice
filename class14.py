# class Student:
    
#     def __init__(self, name, age, cgpa): # constructor
#         self.name = name
#         self.age = age
#         self.cgpa = cgpa
#         # print("Object created successfully")
#         # private pocket_money = 10000
#         print("Initializing")
#         self._pocket_money = 10000

#     def __del__(self):
#         print(f"At last {self.name} destroyed")

#     def purchage_something(self, amount):
#         self._pocket_money = self._pocket_money - amount
#         return self._pocket_money
        # print(f"{self.name} purchased something")
    

# student1 = Student("Ratul", 34, 3.6)
# print(student1.name)
# print(student1)
# print(student1._pocket_money)
# print(student1.purchage_something(200))
# print(student1.purchage_something(500))

# student2 = Student("Sahin", 17, 3.4)

# print(student2.purchage_something(300))



################### INHERITENCE, POLYMORPHISM, SPECIAL MAGIC METHODS ###################

# class Human:
#     pass

# class Student(Human):
#     pass


class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def do_sound(self):
        print("I don't know how to sound")

    def __str__(self): # magic method / dunder method
        return self.name


animal = Animal("Meow", 2, "black")

print(animal.name, animal.age, animal.color)


class Cat(Animal):
    def __init__(self, name, age, color, is_lazy):
        # self.name = name
        # self.age = age
        # self.color = color
        super().__init__(name, age, color)
        self.is_lazy = is_lazy
    
    def do_sound(self):
        print("Meow")

    def __len__(self): # magic method / dunder method
        return int(self.age)


class Dog(Animal):

    def do_sound(self):
        print("Gheu")

    def guard_the_house(self):
        print(f"{self.name} is guarding the house")


mini = Cat("Mini", 1.5, "pink", True)

print(mini.name, mini.age, mini.color, mini.is_lazy)
mini.do_sound()

tommy = Dog("Tommy", 2.5, "Brown")

print(tommy.name, tommy.age, tommy.color)
tommy.do_sound()
tommy.guard_the_house()

cow = Animal("Lali", 3.5, "Red")

cow.do_sound()

print(cow)

print(len(mini))