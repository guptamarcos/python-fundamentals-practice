## Question 1 : Create a frequency dictionary for characters in a string.
# string = "A7xK9mQ2LpZ8rVn4HsT1YwE6cDfJ3uNb0GiPk5RoXaW9MzLt2QhCv7SyFe1UdBn8KjWp4XrTm6NzYa3HsQ9LcVe"
# char_frequency = {}

# for char in string: 
#   if(char_frequency.get(char) == None):
#     char_frequency.update({char: 1})
#   else: 
#     char_frequency[char] += 1

# print(char_frequency)


## Question 2 :  Remove all even numbers from a list.
# numbers = [
#   42, 17, 88, 5, 63, 24, 91, 36, 11, 70,
#   29, 54, 83, 16, 97, 48, 21, 62, 39, 100,
#   7, 56, 13, 80, 45, 32, 99, 18, 73, 64
# ]

# for val in numbers: 
#   if((val%2 )== 0):
#     numbers.remove(val)

# print(len(numbers), numbers)


## Question 3 : Check whether two tuples are identical.

# tup1 = (10,20,30)
# tup2 = (10,20,30)

# print(tup1 == tup2)
# print(tup1 is tup2)


## Question 4 : Find the key with the maximum value in a dictionary.

# inventory = {
#   "Pen": 120,
#   "Notebook": 450,
#   "Pencil": 300,
#   "Eraser": 180,
#   "Marker": 250,
#   "Scale": 210,
#   "Sharpener": 160,
#   "Bag": 95,
#   "Bottle": 140,
#   "Calculator": 750
# }

# max_val = None
# max_val_key = None

# for key,val in inventory.items():
#   if(max_val == None):
#     max_val = val
#     max_val_key = key
#   elif(max_val < val):
#     max_val = val
#     max_val_key = key

# print(max_val ,max_val_key)
  

## Question 5 : Find common elements between two lists using sets.
# numbers1 = [12, 45, 67, 89, 23, 56, 78, 90, 34, 11]
# numbers2 = [90, 45, 100, 78, 23, 200, 11, 300]

# set1 = set(numbers1)
# set2 = set(numbers2)

# print(set1.intersection(set2))


## Question 6 : Find the index of an element in a tuple.

## method 1 
# data = (15, 42, 68, 89, 23, 56, 78, 91, 34, 12, 99)
# print(data.index(42))

## method 2
# data = (15, 42, 67, 89, 23, 56, 78, 91, 34, 12, 99)
# target = 78

# for idx in range(len(data)): 
#   if(target == data[idx]):
#     print(idx)
#     break
