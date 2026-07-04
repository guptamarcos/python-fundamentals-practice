## Question 1: Add a new key-value pair to a dictionary.
# employees = {
#     "emp1": "HR",
#     "emp2": "IT",
#     "emp3": "Finance",
#     "emp4": "IT",
#     "emp5": "HR",
# }

# employees.update({"emp6":"Finance"})
# print(employees)


## Question 2: Remove duplicate elements from a list using a set.
# list1 = [12, 45, 7, 89, 12, 34, 56, 7, 90, 23, 45, 67, 12, 81, 90, 5, 34, 18, 67, 7]
# st = set()

# st.update(list1)
# # for val in list1: 
# #     st.add(val)
    
# print("List ", list1)
# print("Set", st)


## Question 3: Reverse a list without using reverse().
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list1.reverse()
# print(list1)



## Question 4: Find the smallest element in a set.
# tup = (12, 45, 7, 89, 12, 34, 56, 7, 90, 23, 45, 67, 12, 81, 90, 5, 34, 18, 67, 7)
# print(min(tup))



## Question 5: Merge two dictionaries.
# student_basic = {
#     "id": 101,
#     "name": "Aarav Sharma",
#     "age": 21,
#     "course": "B.Tech",
#     "city": "Pune"
# }

# student_academic = {
#     "semester": 6,
#     "cgpa": 8.9,
#     "skills": ["Python", "React", "SQL"],
#     "internship": True,
#     "graduation_year": 2027
# }

# students = {}
# # students.update(student_basic)
# # students.update(student_academic)
# for key,value in student_basic.items():
#     students.update({key: value})

# for key,value in student_academic.items():
#     students.update({key: value})
    
# print(students)



## Question 6: Convert a tuple into a list.
# tup = (12, 45, 7, 89, 12, 34, 56, 7, 90, 23, 45, 67, 12, 81, 90, 5, 34, 18, 67, 7)
# # list1 = list(tup)
# list1 = []
# for val in tup: 
#     list1.append(val)
    
# print(list1)