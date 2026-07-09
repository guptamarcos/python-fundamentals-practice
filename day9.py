## Question 1 : Sort a dictionary by its values.
from operator import itemgetter
my_dict = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items(), key=itemgetter(1)))

print(sorted_dict)


## Question 2 : Count the frequency of each element in a list without using collections.Counter.

# def count_frequency(data):
#   frequency = {}
#   for val in data:
#     if(frequency.get(val) == None):
#       frequency.update({val:1})
#     else:
#       frequency[val] += 1

#   return frequency

# data = [
#   15, 22, 15, 10, 22, 15, 18, 10, 25, 18,
#   22, 30, 15, 10, 25, 22, 18, 30, 15, 40,
#   25, 22, 18, 10, 15, 22, 35, 30, 25, 18
# ]

# frequency = count_frequency(data)
# for key,val in frequency.items():
#   print(f"Key value is : {key} and it's frequency is {val}")



## Question 3 : Create a dictionary from a list of tuples

# def create_dict (data):
#   created_dict = {}
#   for key,val in data:
#     created_dict[key] = val

#   return created_dict

# data = [
#   (101, "Ankit"),
#   (102, "Sneha"),
#   (103, "Rohan"),
#   (104, "Meera"),
#   (105, "Vikas")
# ]

# output = create_dict(data)
# print(output)



## Question 4 : Find the longest word in a list of strings.

# def longest_word(words):
#   maximum_length = float("-inf")
  
#   for word in words:
#     word_length = len(word)
#     if(word_length > maximum_length):
#       maximum_length = word_length
  
#   return maximum_length
  
  
# words = [
#   "algorithm",
#   "data",
#   "structure",
#   "queue",
#   "stack",
#   "binarytree",
#   "graph",
#   "recursion",
#   "backtracking",
#   "dynamicprogramming",
#   "greedy",
#   "memoization",
#   "hashmap",
#   "linkedlist",
#   "multithreading",
#   "serialization",
#   "microservices",
#   "containerization",
#   "virtualization",
#   "authentication",
# ]

# longest_word_length = longest_word(words)
# print(longest_word_length)



## Question 5 : Find whether one set is a subset of another without using issubset().

# def check_is_subset(setA,setB):
#   for valA in setA:
#     flag = False
#     for valB in setB:
#       if(valA == valB):
#         flag = True
    
#     if(not flag):
#       return False
  
#   return True

# setA = {1,2,4}
# setB = {1,2,3,4,5}

# print(check_is_subset(setA,setB))



## Question 6 : Find the missing number from a list containing numbers from 1 to n.

# def missing_number(numbers):
#   total_len = len(numbers)+1
#   total_sum = 0
#   for num in numbers:
#     total_sum += num
  
#   return ((total_len*(total_len+1))/2)-total_sum

# numbers = [12, 9, 7, 1, 3, 5, 11, 2, 4, 10, 6]
# missingNumber = missing_number(numbers)
# print(missingNumber)
