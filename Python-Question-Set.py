#update some program hints:

"""
1. data stucture , stack, queue, data inset pop etc using class
stack queue valo kore dekte hbe...

2. Panagram (A to Z porjonto character ekta word er modde ase 
kina ta funtion diye check kora..)
3. Anagram (duita english word ke kono vabe rearrage kore same kora jay kina practice korte hbe

panagram ,anagram , palindrom eigulo valo vabe practice korte hbe.. obossoi
string method gulo dekte hobe.


django crud niye besi tention na korlew hbe...

+++ nicer program gulo obossoi dekte hbe valo kore 
4-5 ta kore question taqte pare..
"""

stack = []

# def is_pangram(str):
#    word = set({})
#    for x in str:
#       if(x != " "):
#        word.add(x.lower())
    
#    if(len(word) == 26):
#       print("Pangram")
#    else:
#       print("Not Pangram")

# is_pangram('The quick brown fox jumps over the lazy dog')

# def is_anagram(str1,str2):
#     anagram = True
#     if(len(str1) != len(str2)):
#       anagram = False
#     else:
#        for x in str1:
#           if x not in str2:
#              anagram = False
#     if(anagram):
#        print("Anagram")
#     else:
#        print("Not anagram")

# is_anagram('listen','silent')

# # 1) Write a Python function to sum all the numbers in a list
# # Sample list: [8, 2, 3, 0, 7]

# def sum(list):
#     sum = 0
#     for x in list:
#         sum += x
#     return sum
# print(sum([8, 2, 3, 0, 7]))

# # 2) Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
# # Sample list: “The quick Brown Fox”
# # Expected Output :
# # No. of Upper case characters : 3
# # No. of Lower case Characters : 12

# def upper_lower(str):
#     set_value =  set(str)
#     upper = 0
#     lower = 0
#     for x in set_value:
#         if(x.isupper()):
#             upper += 1
#         elif(x.islower()):
#             lower += 1
#     print('No. of Upper case characters : ', upper)
#     print('No. of Lower case characters : ', lower)
# upper_lower('The quick Brown Fox')

# # 3) Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
# # Expected output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# dic = {}
# for key in range(1,16):
#     dic[key] = key * key
# print(dic)

# # 4) Write a Python program to sum all the items in a dictionary
# # Sample dictionary: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

# def sum_dic(dic):
#     sum = 0
#     for x in dic:
#         sum += dic[x]
#     return sum
# print(sum_dic({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}))

# # 5) Write a Python program to create a symmetric difference set of set a and b
# # a = {1, 3, 5, 9, 6}
# # b = {2, 5, 7, 4, 1}
# # Expected output: {3, 2, 7, 9, 6, 4}

# a = {1, 3, 5, 9, 6}
# b = {2, 5, 7, 4, 1}

# c = a.symmetric_difference(b)
# print(c)

# # 6) Write a Python program to remove all elements from a given set.
# # Sample input: {3, 2, 7, 9, 6, 4}
# # Expected output: {}

# a = {3, 2, 7, 9, 6, 4}
# a.clear()
# print(a)

# # 7) If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

# def is_palindrome(word):
#    reverse_word = ''
#    for x in word:
#       reverse_word =  x + reverse_word 
#    if(word == reverse_word):
#          print("yes")
#    else:
#        print("No")
  

# # 9) Write a function that can remove punctuation marks from a string
# #     # punctuations: "!()-[]{};:'"\,<>./?@#$%^&*_~"

# def punctuations_remover(string):
#     punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"
#     fresh_word = ""
#     for char in string:
#         if char not in punctuations:
#             fresh_word += char

#     return fresh_word

# print(punctuations_remover("He,ll.o>"))



# # 10) The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number

# def fibonacci_printer(end_number):
#     list = [0,1]
#     while list[len(list)-1] < end_number:
#          sum = list[len(list)-1]+list[len(list)-2]
#          if sum >= end_number: 
#               break
#          list.append(sum)
#     return list



# # 11) Write a function that can take a sentence and print each word of that sentence in alphabetic order
# # sort_words_alphabetically("hi we are learning python and it's awesome")

# def sort_words_alphabetically(sentence):
#     words = sentence.split(" ")
#     words.sort()
#     for word in words:
#         print(word)
# sort_words_alphabetically("hi we are learning python and it's awesome")


# # 12) Write a function to find even or odd

# def number_checker(number):
#     if number % 2 == 0:
#         print(f"{number} is even number")
#     else:
#         print(f"{number} is odd number")


# # 13) Write a program to check if a number is positive, negative or zero
# def number_checker(number):
#     if number > 0:
#         print("Number given by you is positive")
#     elif number < 0:
#         print("Number given by you is negative")
#     else:
#         print("Number given by you is zero")


# # 14) If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

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



# # 15) Write a function to find the largest number among three given input numbers

# def find_largest_number(*values):
   
#     list_values =  list(values)
#     list_values.sort(reverse=True)
#     print(list_values[0])




# # # A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400. For example,
# #     # 2017 is not a leap year
# #     # 1900 is a not leap year
# #     # 2012 is a leap year
# #     # 2000 is a leap year


# # 16) Now write a function to check if a year is leap year or not

# def check_leapyear(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a leap year")
#     else:
#         print(f"{year} is not a leap year")

# check_leapyear(2009)

