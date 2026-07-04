# # Question 1 : CONVERT A LIST INTO TUPLE 

# list1 = [1,2,3,5,5]
# tup = tuple(list1)

# print(tup, type(tup))


# # Question 2 : REMOVE A ELEMENT FROM THE SET 
# set1 = {1,4,3,5,98,43,33,34,343,65}

# # method 1
# removed_element = set1.pop()

# #method 2
# set1.remove(4)

# #method 3
# set1.discard(98)

# print(set1)


## Question 3 : REMOVE A KEY FROM DICTIONARY 
# dictionary = {
#   "name": "Gauri Shankar",
#   "course": "B.tech",
#   "age": 20,
# }

## method 1 
# del dictionary["course"]
# print(dictionary)

## method 2
# removed_key_val = dictionary.pop("age")
# print(removed_key_val, dictionary)

## method 3 
# removed_key_val_pair = dictionary.popitem()
# print(removed_key_val_pair, dictionary)


## Question 4 : FIND THE SUM OF ALL NUMBERS IN THE LIST 

## method 1
# list1 = [1,2,3,5,5]
# print(sum(list1))

## method 2
# list_sum = 0
# for val in list1: 
#   list_sum += val

# print(list_sum)


## Question 5 : CHECK A DICTIONARY CONTAINS THE A KEY OR NOT 
# dictionary = {
#   "name": "Gauri Shankar",
#   "course": "B.tech",
#   "age": 20,
# }

# key_name = input("Enter the key value: ")
# found_value = dictionary.get(key_name)
# print("Key Value pair not exist" if (found_value == None) else found_value)


## Question 6 : PRINT ALL ELEMENT OF TUPLE USING LOOP
# tup = (2,4,3,4,2,4,3,2,45,7,4,34,6,34,345)
# for i in range (0, len(tup)):
#   print(i+1,tup[i])




