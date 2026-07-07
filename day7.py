## Question 1 : Check whether a list is a palindrome.
# def checkPalindrome (string):
#   string = string.strip()
#   str_len = len(string)

#   if(str_len == 0 ):
#     print("String is empty")
#   elif(str_len == 1 ):
#     print("String is Palindrome")
#   else:
#     start = 0
#     end = str_len-1
#     flag = True

#     while(start < end) :
#       if(string[start] != string[end]):
#         flag = False
#         print("String is not a palindrome")
#         break
#       start += 1
#       end -= 1

#     if(flag):
#       print("String is Palindrome")


# string = input("Please enter the string: ")
# checkPalindrome(string)


## Question 2 : Find all duplicate elements in a list.
# def findDuplicates(nums):
#   nums_len = len(nums)

#   duplicate_elements = {}
#   for val in nums:
#     if (duplicate_elements.get(val) == None):
#       duplicate_elements.update({val:1})
#     else:
#       duplicate_elements[val] += 1


#   return list(duplicate_elements.keys())


# duplicate_elements = findDuplicates([
#     12, 45, 67, 12, 89, 23, 45, 90, 11, 67,
#     34, 56, 78, 90, 23, 45, 100, 11, 12, 56,
#     78, 99, 101, 34, 45, 12, 90, 78, 56, 102
# ])

# print(duplicate_elements)

## Question 3 : Store student names and marks in a dictionary and print students scoring above 75.
# students = {
#     "A": 76,
#     "B": 34,
#     "C": 88,
#     "D": 100,
#     "E": 74,
#     "F": 81,
#     "G": 79,
#     "H": 75,
#     "I": 60,
#     "J": 95,
# }

# for key,val in students.items():
#   if(val > 75):
#     print(key)


## Question 4 : Find the maximum and minimum values in a dictionary.
# exam_scores = {
#     "Student1": 88,
#     "Student2": 76,
#     "Student3": 95,
#     "Student4": 91,
#     "Student5": 68,
#     "Student6": 95,
#     "Student7": 68,
#     "Student8": 84,
# }

# min_val = float("inf")
# max_val = float("-inf")

# for key,val in exam_scores.items():
#   if(val > max_val):
#     max_val = val
#   elif (val < min_val):
#     min_val = val

# print(min_val, max_val)

## Question 5 : Merge two lists into a dictionary where one list contains keys and the other contains values.
# student_ids = [101, 102, 103, 104, 105, 106]
# student_names = ["Aman", "Priya", "Rohit", "Neha", "Karan", "Anjali"]

# student_dict = {}

# for idx in range(len(student_ids)):
#   student_dict[student_ids[idx]] = student_names[idx]

# print(student_dict)


## Question 6 : Remove duplicate dictionaries from a list of dictionaries.
# records = [
#     {"id": 1, "name": "Alice", "city": "Delhi"},
#     {"id": 2, "name": "Bob", "city": "Mumbai"},
#     {"id": 3, "name": "Charlie", "city": "Pune"},
#     {"id": 1, "name": "Alice", "city": "Delhi"},
#     {"id": 4, "name": "David", "city": "Hyderabad"},
#     {"id": 2, "name": "Bob", "city": "Mumbai"},
#     {"id": 5, "name": "Eva", "city": "Chennai"},
#     {"id": 3, "name": "Charlie", "city": "Pune"},
#     {"id": 6, "name": "Frank", "city": "Kolkata"},
# ]

# new_records = []

# for item in records: 
#   if(not(item in new_records)):
#     new_records.append(item)

# print(new_records)
    
