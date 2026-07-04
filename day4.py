## Question 1 : Find the union of two sets.

## method 1
# set1 = {1,2,3}
# set2 = {4,5,6}
# set3 = set1.union(set2)
# print(set3)

## method 2
# set1 = {1,2,3}
# set2 = {4,5,6}
# set3 = set()

# for val in set1:
#   set3.add(val)

# for val in set2:
#   set3.add(val)

# print(set3)


## Question 2 : Find the intersection of two sets.

# set1 = {2, 32, 42, 3, 4}
# set2 = {43, 35, 32, 42, 3}
# set3 = set1.intersection(set2)
# print(set3)


## Question 3 : Find the second largest number in a list.

# list1 = [15, 22, 8, 19, 31, 27]
# first_max = max(list1)
# second_largest = float("-inf")

# for val in list1 :
#   if((val != first_max) and (val > second_largest)):
#     second_largest = val

# print("Second largest value is : ", second_largest)


## Question 4 : Find all keys whose value is greater than 50 in a dictionary.

# marks = {"Alice": 78, "Bob": 45, "Charlie": 90, "David": 32, "Eva": 67}
# list1 = []

# for key,value in marks.items():
#   if(value > 50):
#     list1.append(key)
    
# print(list1)


# Question 5 : Sort a list without using the built-in sort() method.
# list1 = [23, 45, 12, 67, 34, 89, 56]

# for i in range(0,len(list1)):
#   min_val_idx = i
#   for j in range(i+1, len(list1)):
#     if(list1[min_val_idx] > list1[j]):
#       min_val_idx = j
  
#   curr_idx_val = list1[i]
#   list1[i] = list1[min_val_idx]
#   list1[min_val_idx] = curr_idx_val
  
# print(list1)
    
  
# Question 6 : Find elements that are present in one set but not the other.
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

## method 1
# print(set1-set2)

## method 2
# set3 = set()
# for val1 in set1:
#   flag = True
#   for val2 in set2:
#     if(val1 == val2):
#       flag = False
  
#   if(flag):
#     set3.add(val1)
    
# print(set3)
