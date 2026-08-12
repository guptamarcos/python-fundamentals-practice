## Question 1: Write a recursive function to find the maximum element in a list.
# def max_element(list1,curr_max,curr_idx):
#   if(curr_idx >= len(list1)):
#     return curr_max

#   if(list1[curr_idx] > curr_max):
#     curr_max = list1[curr_idx]

#   return max_element(list1,curr_max,curr_idx+1)

# num_list = list(map(int,input("Enter the numbers: ").split(" ")))
# print(max_element(num_list,float("-inf"),0))


## Question 2: Write a recursive function to reverse a string.
# str_val = "hello"
# print(str_val[::-1])
# def reverse_string(str_val,curr_idx):
#   if(curr_idx == 0):
#     return str_val[0]

#   return str_val[curr_idx] + reverse_string(str_val,curr_idx-1)

# str1 = input("Enter the string: ")
# print(reverse_string(str1,len(str1)-1))


## Question 3: Write a recursive function to check whether a string is a palindrome.
# def check_palindrome(str,s_idx,e_idx):
#   if(s_idx >= e_idx):
#     return True

#   if(str[s_idx] != str[e_idx]):
#     return False

#   return check_palindrome(str,s_idx+1,e_idx-1)

# str1 = input("Enter the string: " )
# s_idx = 0
# e_idx = len(str1)-1
# print(check_palindrome(str1,s_idx,e_idx))

## Question 4: Write a recursive function to count the number of digits in an integer.
# ASSUMING LEADING ZEROS IS NOT THE PART OF NUMBER

# def count_digits(curr_num):
#   if (curr_num == 0):
#     return 0

#   curr_num = int(curr_num/10)
#   return 1 + count_digits(curr_num)

# num = int(input("Enter the number: "))
# print(count_digits(num))

## Question 5: Write a recursive function to calculate x^n without using **.
# def calc_expo(num_val,power_val):
#   if(power_val == 0):
#     return 1

#   if(power_val == 1):
#     return num_val

#   return num_val * calc_expo(num_val,power_val-1)

# num_val,power_val = map(int,input("Enter the num_val and power_val: ").split(" "))
# print(calc_expo(num_val,power_val))

## Question 6: Write a recursive function to find the nth Fibonacci number.
# Assuming position idx is start from 0
# 0 1 1 2 3 5 8 ...
# n --> position
# def fibonacci(n):
#   if (n == 0 or n == 1):
#     return n

#   return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter the position number: "))
# print(fibonacci(n))

# Question 7: Write a recursive function to find the greatest common divisor (GCD) of two numbers.
# def gcd(a, b):
#   if b == 0:
#     return a

#   return gcd(b, a % b)

# print(gcd(48, 18))


# Question 8: Write a recursive function to count how many times a particular element occurs in a list.
# num_list = list(map(int,input("Enter the list numbers: ").split(" ")))
# element = int(input("Enter the element: "))

# def count_occurance(element,element_count,curr_idx):
#   if(num_list[curr_idx] == element):
#     element_count += 1

#   if(curr_idx == len(num_list)-1):
#     return element_count

#   return count_occurance(element,element_count,curr_idx+1)


# print(f"Total occurance of {element} in the given list is {count_occurance(element,0,0)}")

# Question 9: Write a recursive function to find the first occurrence of an element in a list.
# num_list = list(map(int,input("Enter the list numbers: ").split(" ")))
# element = int(input("Enter the element: "))

# def first_occurance(curr_idx):
#   if(curr_idx == len(num_list)):
#     return -1

#   if (num_list[curr_idx] == element):
#     return curr_idx

#   return first_occurance(curr_idx+1)

# print(f"First occurance of {element} in list is {first_occurance(0)}")
