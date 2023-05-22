# https://drive.google.com/drive/folders/1skV6OretMOimPgDSomSSjw1tVI2kMMfw

# def is_palindrome(word):
#    reverse_word = ''
#    for x in word:
#       reverse_word = reverse_word + x
#    if(word == reverse_word):
#          print("yes")
#    else:
#        print("No")
# is_palindrome('eye')


# def convert_to_miles(kilometers):
#     if (type(kilometers) not in [float, int]):
#         raise TypeError("Please enter kilometers as a number")
#     return kilometers * 0.621371

# print(convert_to_miles(5))

# def punctuations_remover(string):
#     punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"
#     fresh_word = ""
#     for char in string:
#         if char not in punctuations:
#             fresh_word += char

#     return fresh_word

# print(punctuations_remover("He,ll.o>"))

# def fibonacci_printer(end_number):
#     a, b = 0, 1
#     count = 0
#     while count < end_number:
#         a, b = b, a + b
#         print(b)
#         count += 1

# fibonacci_printer(10)


# def sort_words_alphabetically(sentence):

#     words = sentence.split(" ")

#     words.sort()

#     for word in words:
#         print(word)


# sort_words_alphabetically("hi we are learning python and it's awesome")

# def number_checker(number):
#     if number % 2 == 0:
#         print(f"{number} is even number")
#     else:
#         print(f"{number} is odd number")

# number_checker(5)


# def number_checker(number):
#     if number > 0:
#         print("Number given by you is positive")
#     elif number < 0:
#         print("Number given by you is negative")
#     else:
#         print("Number given by you is zero")

# number_checker(-9)

# def is_prime(number):
#     if number > 1:
#         prime = True
#         for x in range(2,number):
#             if(number%x == 0):
#                 prime = False
#                 break
#         if(prime):
#             print("Prime")
#         else:
#             print('Not prime')

#     else:
#         print('Not prime')

# is_prime(4)

# def find_largest_number(*values):
   
#     list_values =  list(values)
#     list_values.sort(reverse=True)
#     print(list_values[0])

# find_largest_number(15, 23, 8)

# def check_leapyear(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# check_leapyear(2009)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)

