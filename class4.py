student1_name = "Sakib al hasan - eve"
student2_name = "Nannu"

if student2_name.endswith("eve"):
    student2_name = student2_name.replace("reg", "eve")
    print("Student from evening batch")
    # print("Hello")
    # print("Hi")

# a = "", 0, None, False # falsy value
#  "hello", 23, 1.45, -3 # truthy value

# c = [1, 2, 3, 4]
# print(len(c))

# if len(c):
#     student2_name = student2_name.replace("reg", "eve")
#     print("Student from evening batch")
#     # print("Hello")
#     # print("Hi")

# print(student2_name)

# if student2_name.endswith("reg"):
#     print("Student from Regular batch")
    
#     # if student2_name.find("Nannu"):
#     if student2_name.startswith("Nannu"):
#         print("Helo Nannu")
#     else:
#         print("Sorry, Nannu. Better luck next time")

# else:
#     print("Student from Evening batch")

# if student2_name.endswith("reg"):
#     print("Student from Regular batch")
# elif student2_name.endswith("eve"):
#     print("Student from Evening batch")
# else:
#     print("Something went wrong. Please contact with admission section")

# print("Student from regular batch") if student2_name.endswith("reg") else print("student from evening batch") if student2_name.endswith("eve") else print("Something went wrong. Please contact with admission secion")


# print("Out of if block")

["George Arnob - eve", "Badsha - reg", "Sazzat - eve"]

print("Sazzat - reg")
a="Sazzat - eve"
print(a[9:12])
print(a[-3:-1])
print(a[-3:])
print(a.endswith('eve'))
print(a[-3:] == "eve")

# check the batch
# if evening make sure sazzat is there

if a.endswith("eve"):
    print("Evening batch")
    # if a.find("Sazzat") >= 0:
    if a.find("Sazzat") != -1:
        print("Sazzat is in the evening batch")
elif a.endswith("reg"):
    print("Regular batch")
else:
    print("Unknown batch")

# print("Sazzat is in the evening batch".find("odd"))

# 1, 2, 3, "a", "b", "bye", True # truthy value

# 0, False, "", None, -5 # falsy value

# if a.endswith("eve"):
#     dfsdfdsfsd
#     dfsdfsdfds

# money = 1000

# if money > 0 and money <= 5:
#     print("You've some money")
# elif money > 100:
#     print("You're super rich")
# elif money > 5:
#     print("You're rich")
# else:
#     print("You're poor")
