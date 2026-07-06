## Question 1: Rotate a list to the left by one position.

## method 1
# nums = [22, 33, 44, 55, 66, 77, 11]
# last_element = nums.pop()
# nums.insert(0,last_element)

## method 2
# nums = ['apple', 'banana', 'mango', 'grape']

# last_element = nums[len(nums)-1]
# last_element_idx = len(nums)-1

# for i in range(last_element_idx, 0, -1):
#   nums[i] = nums[i-1]

# nums[0] = last_element
# print(nums)


## Question 2: Count the number of unique words in a sentence.
# sentence = "  the quick brown fox jumps over the lazy dog"
# unique_words = set(sentence.strip().split(" "))
# print(unique_words, len(unique_words))


## Question 3: Swap the first and last element of a list.
# nums = [12, 45, 7, 89, 23, 56, 91, 34]

# last_element = nums[len(nums)-1]
# nums[len(nums)-1] = nums[0]
# nums[0] = last_element

# print(nums)


## Question 4: Invert a dictionary (swap keys and values).
# student_marks = {"Alice": 90, "Bob": 85, "Charlie": 95, "David": 88}
# swapped_dict = {}

# for key,value in student_marks.items():
#   swapped_dict.update({value:key})

# print("Original Dictionary is: ", student_marks)
# print("Swapped Dictionary is : ", swapped_dict)
  

## Question 5: Find the symmetric difference of two sets.
# set1 = {2, 4, 6, 8, 10}
# set2 = {1, 2, 3, 4, 5}

# common_elements = set1.intersection(set2)

# print("Symmetric elements of set1 is ", set1-common_elements)
# print("Symmetric elements of set2 is ", set2-common_elements)



## Question 6: Find the average of all elements in a list.

## method 1
# numbers = [91, 13, 57, 24, 68, 35, 79, 46]
# print(sum(numbers)/len(numbers))

# method 2
# numbers = [91, 13, 57, 24, 68, 35, 79, 46]
# total_sum = 0

# for val in numbers: 
#   total_sum += val
  
# avg_val = total_sum/len(numbers)
# print(avg_val)

