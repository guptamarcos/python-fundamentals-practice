## Question 1: Group duplicate values together in a dictionary.
# def combine_dict_values(data):
#   new_dict = {}
#   for key,val in data.items():
#     if(new_dict.get(val) == None):
#       new_dict.update({val: [key]})
#     else:
#       new_dict[val].append(key)

#   return new_dict

# data = {
#   "Laptop": "Electronics",
#   "Phone": "Electronics",
#   "Table": "Furniture",
#   "Chair": "Furniture",
#   "Sofa": "Furniture",
#   "Milk": "Grocery",
#   "Bread": "Grocery",
#   "Eggs": "Grocery",
#   "TV": "Electronics"
# }
# new_dict = combine_dict_values(data)
# print(new_dict)



## Question 2: Find the element that appears only once while all others appear twice.
# def find_number(numbers):
#   ans = numbers[0]

#   for i in range(1,len(numbers)):
#     ans = ans^numbers[i]
   
#   return ans  

# numbers = [23, 45, 67, 89, 23, 45, 12, 34, 56, 78, 89, 12, 34, 56, 78, 67, 91]
# ans = find_number(numbers)
# print(ans)



## Question 3: Implement a simple inventory system using a dictionary (add, update, delete, search products).
# def add_inventory(inventory):
#   key_name = int(input("Enter the key : "))
#   while(inventory.get(key_name) != None):
#     print("Key already exist , Please Enter the different key ")
#     key_name = int(input("Re-Enter the key : "))
  
#   product_name = input("Enter the product name: ")
#   product_price,product_quantity = map(int,input("Enter the price , quantity : ").split(" "))
   
#   key_value = {
#     "name": product_name,
#     "price": product_price,
#     "quantity": product_quantity
#   }
  
#   inventory.update({key_name:key_value})
#   print("Product added successfully in inventory")
#   return inventory
  
  
# def update_inventory(inventory):
#   product_id = int(input("Enter the product_id : "))
#   while(inventory.get(product_id) == None):
#     print("Product id not exist, Please enter the valid product id ")
#     product_id = int(input("Re-Enter the product id : "))
    
#   product_name = input("Enter the new name for product: ")
#   product_price,product_quantity = tuple(map(int,input("Enter the price , quantity : ").split(" ")))
    
#   inventory[product_id] = {
#     "name": product_name,
#     "price": product_price,
#     "quantity": product_quantity,
#   }
#   return inventory
  
  
# def delete_inventory(inventory):
#   product_id = int(input("Enter the product_id : "))
#   while(inventory.get(product_id) == None):
#     print("Product id not exist, Please enter the valid product id ")
#     product_id = int(input("Re-Enter the product id : "))
    
#   del inventory[product_id]
#   print("Product deleted successfully")
#   return inventory


# def search_inventory(inventory):
#   product_id = int(input("Enter the product_id : "))
#   value = inventory.get(product_id)
  
#   if(value == None):
#     print("Invalid product id , product not found ")
#     return 
  
#   print(value)


# inventory = {
#   201: {"name": "Laptop", "price": 62000, "quantity": 8},
#   202: {"name": "Mouse", "price": 650, "quantity": 50},
#   203: {"name": "Keyboard", "price": 1500, "quantity": 22},
#   204: {"name": "Monitor", "price": 18000, "quantity": 7},
#   205: {"name": "Webcam", "price": 3200, "quantity": 15},
#   206: {"name": "USB Hub", "price": 1200, "quantity": 40},
#   207: {"name": "SSD", "price": 5200, "quantity": 18},
#   208: {"name": "HDD", "price": 4300, "quantity": 14},
#   209: {"name": "Graphics Card", "price": 42000, "quantity": 5},
#   210: {"name": "RAM", "price": 3600, "quantity": 28}
# }

# operation_name = input("Which operation do you want to perform ?\n For add type add \n For update type update \n For delete type delete \n For search type search \n")

# operation_name = operation_name.strip().lower()

# if   (operation_name == "add"):
#   inventory = add_inventory(inventory)
# elif (operation_name == "update"):
#   inventory = update_inventory(inventory)
# elif (operation_name == "delete"):
#   inventory = delete_inventory(inventory)
# elif (operation_name == "search"):
#   search_inventory(inventory)
# else:
#   print("Invalid operation name")


# print(inventory)



## Question 4: Given a list of tuples (student, subject, marks), create a nested dictionary.
# def create_dict(records):
#   new_dict = {}
#   for record in records:
#     if(new_dict.get(record[0]) == None):
#       new_dict.update({record[0]: {record[1]: record[2]}})
#     else:
#       new_dict[record[0]].update({record[1]: record[2]})
      
#   return new_dict
  
# records = [
#   ("Gauri", "Python", 95),
#   ("Riya", "Python", 91),
#   ("Aman", "Python", 88),
#   ("Gauri", "FastAPI", 93),
#   ("Riya", "FastAPI", 89),
#   ("Aman", "FastAPI", 90),
#   ("Gauri", "PostgreSQL", 94),
#   ("Riya", "PostgreSQL", 92),
#   ("Aman", "PostgreSQL", 87),
#   ("Gauri", "React", 90),
#   ("Riya", "React", 88),
#   ("Aman", "React", 91)
# ]

# new_dict = create_dict(records)
# print(new_dict)



## Question 5: Given two dictionaries, merge them such that values of common keys are added together.
# def merge_dict(dict1,dict2):
#   new_dict = {}

#   for key,val in dict1.items():
#     if(new_dict.get(key) == None):
#       new_dict.update({key:val})
#     else :
#       new_dict[key] += val

#   for key,val in dict2.items():
#     if(new_dict.get(key) == None):
#       new_dict.update({key:val})
#     else :
#       new_dict[key] += val

#   return new_dict

# dict1 = {}
# dict1_len = int(input("Enter the number of key, value pair in dict1: "))
# for i in range(dict1_len):
#   key = input(f"Enter the {i+1} key : ")
#   val = int(input("Enter the value of the key: "))

#   if(dict1.get(key) == None):
#     dict1.update({key:val})
#   else:
#     dict1[key] += val


# dict2 = {}
# dict2_len = int(input("Enter the number of key, value pair in dict2: "))
# for i in range(dict2_len):
#   key = input("Enter the key value: ")
#   val = int(input("Enter the value of the key: "))

#   if(dict2.get(key) == None):
#     dict2.update({key:val})
#   else:
#     dict2[key] += val


# new_dict = merge_dict(dict1,dict2)
# print(new_dict)



## Question 6: Given a paragraph, find the top 5 most frequent words using dictionaries and sort them by frequency.
# import string
# from operator import itemgetter

# text = "FastAPI is a modern Python framework for building APIs. FastAPI provides automatic documentation, high performance, and simple development. Developers choose FastAPI because FastAPI supports asynchronous programming, integrates well with databases, and makes API development faster. Building APIs with FastAPI improves productivity and reduces development time."

# translator = str.maketrans("", "", string.punctuation)

# clean_text = text.translate(translator).split(" ")

# my_dict = {}
# for word in clean_text:
#   if(my_dict.get(word) == None):
#     my_dict.update({word: 1})
#   else:
#     my_dict[word] += 1

# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

# i = 1
# for key,value in sorted_dict.items():
#   print(f"{key}: {value}")
#   if (i==5):
#     break
#   i += 1