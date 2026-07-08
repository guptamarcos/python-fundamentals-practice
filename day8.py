## Question 1: Find the first non-repeated element in a list.
# def non_repeated_element(numbers):

#   set1 = {}

#   for num in numbers:
#     if(set1.get(num) == None):
#       set1.update({num: 1})
#     else :
#       set1[num] += 1

#   for key,val in set1.items():
#     if(val == 1):
#       print(key)
#       break

## [12, 15, 12, 18, 20, 15, 18, 25]
# numbers = list(map(int,input("Enter the values: ").split(" ")))
# print(type(numbers))


## Question 2: Group words by their first letter using a dictionary.
# def group_words(words):
#   word_dict = {}

#   for val in words:
#     first_char = val[0]

#     if(word_dict.get(first_char) == None):
#       word_dict.update({first_char: [val]})

#     else:
#       word_dict[first_char].append(val)

#   return dict(sorted(word_dict.items()))


# words = [
#   "apple", "ant", "arrow",
#   "banana", "ball", "boat",
#   "cat", "camel", "circle",
#   "dog", "door", "duck",
#   "elephant", "eagle", "earth",
#   "fish", "frog", "flag",
#   "goat", "grape", "gold",
#   "hat", "horse", "house",
#   "ice", "iron", "igloo",
#   "joker", "jam", "jungle"
# ]

# word_dict = group_words(words)
# print(word_dict)

## Question 3: Find whether two lists contain the same elements regardless of order.
# list1 = [1, 1, 2, 2, 3, 4, 5, 5]
# list2 = [5, 4, 3, 2, 1, 5, 2, 1]

# duplicates = {}
# for val in list1:
#   if(duplicates.get(val) == None):
#     duplicates.update({val:1})
#   else:
#     duplicates[val] += 1

# for val in list2:
#   if(duplicates.get(val) != None):
#     print("True")
#     break


## Question 4: Find the difference between two dictionaries (keys present in one but not the other).
# dict1 = {
#   "math": 91,
#   "science": 88,
#   "english": 94,
#   "history": 76,
#   "geography": 82,
#   "computer": 99,
# }

# dict2 = {
#   "science": 90,
#   "english": 95,
#   "physics": 87,
#   "chemistry": 84,
#   "computer": 98,
#   "biology": 89,
# }

# set1 = set(dict1.keys())
# set2 = set(dict2.keys())

# print(set1-set2)


## Question 5: Flatten a nested list of integers.
# method 1
# nested_list = [
#   [1, 2, 3],
#   [4, 5],
#   [6],
#   [7, 8, 9]
# ]

# flatten_list = []

# for sublist in nested_list:
#   for val in sublist: 
#     flatten_list.append(val)


# print(flatten_list)

# method 2
# def flatten_list(nums):
#   flattened_list = []
#   for item in nums:
#     if(isinstance(item,list)):
#       result = flatten_list(item)
#       flattened_list.extend(result)
#     else:
#       flattened_list.append(item)
      
#   return flattened_list
  
# nested = [1, [2, [3, [4]], 5], 6]
# flattened_list = flatten_list(nested)
# print(flattened_list)
    

## Question 6: Find all pairs in a list whose sum equals a given target.
# def find_pairs(nums,target):
#   pairs_set = set()
#   for i in range(len(nums)):
#     target_element = target-nums[i]
    
#     for j in range(i+1, len(nums)):
#       if(nums[j] == target_element):
#         pairs_set.add((nums[i],nums[j]))
        
#   return pairs_set
  
# numbers = [21, 4, 17, 8, 13, 9, 5, 16, 12, 1, 20, 7, 3]
# print(find_pairs(numbers,21))