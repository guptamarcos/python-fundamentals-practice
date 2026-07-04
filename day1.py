## Question 1: Create a list of 10 numbers and print the largest number.
# list = [42, 817, 156, 903, 274, 691, 58, 432, 785, 129]

# max_val = -1
# i = 0

# while (i<len(list)):
#   if(max_val < list[i]):
#     max_val = list[i]
#   i += 1

# print(max_val)


## Question 2: Create a tuple containing the names of five cities and print the third city.
# tuple = ("Delhi","Mumbai","Bengaluru","Hyderabad","Chennai")

# for i in range (5):
#   if(i==2):
#     print(tuple[i])
#     break


## Question 3: Create a dictionary of student names and their marks. Print the marks of a particular student.
# students = {
#     "Aarav": {"marks": 88},
#     "Rohit": {"marks": 76},
#     "Mohit": {"marks": 91},
#     "Atul": {"marks": 67},
#     "Divayam": {"marks": 82},
# }

# dict_keys = students.keys()
# # print(dict_keys)
# for key in dict_keys:
#     print(students[key].get("marks"))


# print(type(dict_keys))


## Question 4: Create a set of numbers and check whether a given number exists.
# set1 = {83, 12, 67, 45, 90, 5, 31, 76, 58, 24}

# def check_element(num,set):
#     flag = False
#     for val in set:
#         if(num == val):
#             flag = True
#             break

#     if(flag):
#         print("Element is found")
#     else:
#         print("Element is not found")


# check_element(24,set1)


## Question 5: Find the length of a list without using len().
# list1 = [12, 45, 7, 89, 12, 34, 56, 7, 90, 23, 45, 67, 12, 81, 90]
# list_len = 0

# for i in range(0,len(list)):
#   list_len += 1
  
# print("List length is ", list_len)



## Question 6: Count how many times an element appears in a tuple.
# tup = (12, 45, 7, 89, 12, 34, 56, 7, 90, 23, 45, 67, 12, 81, 90, 5, 34, 18, 67, 7)

# num = 12
# count = 0
# for val in tup:
#     if(val==num):
#         count += 1

# print(count)
# print(tup.count(12))
