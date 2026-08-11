## Question 1: Find the third largest unique element in a list.
# num_list = list(map(int, input("Enter you list elements: ").split(" ")))

# # num_list.sort()
# # print(num_list[2])

# first_largest = float("-inf")
# second_largest = float("-inf")
# third_largest = float("-inf")

# for i in range(0,len(num_list)):
#   curr_num = num_list[i]
#   if (curr_num > first_largest):
#     third_largest = second_largest
#     second_largest = first_largest
#     first_largest = curr_num
#   elif (curr_num < first_largest and curr_num > second_largest):
#     third_largest = second_largest
#     second_largest = curr_num
#   elif (curr_num > third_largest):
#     third_largest = curr_num
    

# print(f"1st largest value is: {first_largest} \n 2nd largest value is: {second_largest} \n 3rd largest value is: {third_largest}")
    
  
## Question 2: Move all zeros in a list to the end while maintaining the order of other elements.
# num_list = list(map(int,input("Enter the list elements: ").split(" ")))
# ans_list = [0]*len(num_list)

# idx = 0
# for i in range(0,len(num_list)):
#   if(num_list[i] != 0):
#     ans_list[idx] = num_list[i]
#     idx += 1
    
# print(ans_list)


## Question 3: Find the elements that appear in all three given lists.
# list1 = [1, 2, 3, 4, 5]
# list2 = [2, 3, 6, 7]
# list3 = [2, 3, 8, 9]

# common_nums_list1 = []
# ans_list = []

# for i in range(0,len(list1)):
#   for j in range(0, len(list2)):
#     if(list1[i] == list2[j]):
#       common_nums_list1.append(list1[i])
#       break
    
# for i in range(0,len(common_nums_list1)):
#   for j in range(0,len(list3)):
#     if(list3[j]  == common_nums_list1[i]):
#       ans_list.append(list3[j])
      
  
# print(ans_list)



## Question 4: Write a recursive function to calculate the factorial of a number.
# def fact(num):
#   if(num == 0 or num == 1):
#     return num
  
#   return num*fact(num-1)

# num = int(input("Enter the number: "))

# ans = fact(num)
# print(ans)

## Question 5: Write a recursive function to calculate the sum of numbers from 1 to n."E"
# def sum(num):
#   if (num == 1):
#     return num
  
#   return num + sum(num-1)

# num = int(input("Enter the value of n: "))
# ans = sum(num)

# print(f"Sum of numbers from 1 to {num} is {ans}")

## Question 6: Write a recursive function to calculate the sum of all elements in a list.
# def sum_of_list(num_list, curr_idx):
#   if(len(num_list) == 1):
#     return num_list[0]
  
#   if(curr_idx >= len(num_list)):
#     return 0
  
#   return num_list[curr_idx] + sum_of_list(num_list,curr_idx+1)
    

# num_list = list(map(int,input("Enter the elements of the list: ").split(" ")))
# list_sum = sum_of_list(num_list,0)
# print("The sum of the list element is :",list_sum)




  