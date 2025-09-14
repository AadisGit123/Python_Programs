# a=10
# if a!=10:
#   print('a is not 10')
# else:
#   print('a is 10')

# print('Happy New year in :')
# for x in range(10,0,-1):
#   print(x)
# print("Happy New Year !!!")

# fruits = ["apple", "banna", "grapes", "mango"]

# print(fruits[0])
# for x in fruits:
#   print(x)

# num_pad=((1,2,3),
#           (4,5,6),
#           (7,8,9),
#           ("*",0,"#"))
# for row in num_pad:
#   for num in row:
#     print(num, end=" ")
#   print()
##
# capitals={"USA":"Whashington DC",
#           "India": "New Delhi",
#           "Japan":"Tokyo",
#           "Russia":"Moscow"}
# print(capitals.get("USA"))
# capitals.update({"France":"Paris"})
# capitals.pop("USA")
# capitals.popitem()
# print(capitals.keys())  
# print(capitals)
# print(capitals.items()})
# print(capitals.values())
# print(capitals.keys())
### for i in range(10):
#  print(f"{random.randrange(9)}", end=" ")
# def net_price(list_price,discount=0,tax=.18):
#   return list_price*(1+tax)*(1-discount)
# print(net_price(500))
### def hello(greeting,title,first,last):
#   return(f"\n{greeting} {title}{first} {last}\n")
# print(hello(greeting="Hello",first="Ethan",title="Mr.",last="Hunt"))
### print("aadi","tya",sep="-")
### def Sum(*args):
#   sum=0
#   for arg in args:
#     sum+=arg
#   return sum
# print(f"Sum = {Sum(1,3,4,5,5)}")
##
# # def address(*args,**kwargs):
#   for arg in args:
#      print(arg,end=" ")
#   for key,value in kwargs.items():
#       print(f"\n{key}: {value}",end=" ")
### address("Ethan","Hunt",
#         street="14",
#         city="Mumbai",
#         state="Sydney",
#         zip="080")
### quodrople=[x * 4 for x in range(1,11)]
# square=[y * y for y in range(1,11)]
# print(square)
### # fruits = ["apple", "banna", "grapes", "mango"]   
# fruits=[fruit.capitalize() for fruit in fruits]
# print(fruits)                                   
### help("modules") -->returns the libraries
# def fun1():
#   x=1
#   def fun2():
#     print(x)
# fun2()
# fun1()
### import random
# slots=["🔔","💀","⚽️","🍒","⭐️"]
# print(random.choice(slots) for slot in range(3))
##
# import time

# print(time.ctime())

##
# a = [3,2,4,1]
# # a.sort()
# # print(a)
# # a.sort(reverse=True)
# # print(a)
# a.reverse()
# print(a)

##
# def Search(name,a):
#   if name in a.keys():
#     DOB = a.value(name)
#     print (f"{name}:{DOB}")
#   else:
#     print(f"{name} not found").strip()
#     a.apend(name)
#     input(a.update("Enter the Date of Birth: ")).strip()
#     if name in a.keys():
#       print("Name and DOB added successfully")
 
# a = {}   
# n = int(input("Enter the number of entities: "))
# print("Enter the Entities: ")
# for i in range(n):
#   name = input(f"Key: ").strip()
#   dob = input(f"Value: ").strip()
#   a[name] = dob
  
# N = input("Enter the name to be searched: ")
# Search(N, a)

##    
# def search_or_add(name_dict, name):
#     name = name.strip()
#     if name in name_dict:
#         print(f"{name}'s Date of Birth is: {name_dict[name]}")
#     else:
#         dob = input(f"{name} not found. Please enter their Date of Birth (DD-MM-YYYY): ").strip()
#         name_dict[name] = dob
#         print(f"{name} has been added with DOB: {dob}")

# dob_dict = {}

# n = int(input("How many entries would you like to add initially? "))

# for i in range(n):
#     name = input(f"Enter name #{i+1}: ").strip()
#     dob = input(f"Enter DOB for {name} (DD-MM-YYYY): ").strip()
#     dob_dict[name] = dob

# print("\nYou can now search for names. Type 'exit' to stop.\n")

# while True:
#     name_input = input("Enter a name to search: ").strip()
#     if name_input.lower() == 'exit':
#         break
#     search_or_add(dob_dict, name_input)

# print("\nFinal Dictionary:")
# for name, dob in dob_dict.items():
#     print(f"{name}: {dob}")
##
# def printing(n):
#   print(n)

# n = [1, 2, 3, 4, 5]
# do = list(map(printing,n))
##Files in Python
# File = "File.txt"
# with open(File,"w") as F:
#   F.write("This looks like a job for me ")
  
# with open(File,"a") as F:
#   F.write("so, everybody just follow me.")
  
# with open(File,"a") as F:
#   F.write("\nCause, we need a little bit of controversy, ")
  
# with open(File,"a") as F:
#   F.write("cause, it feels so empty without me")
  
# with open(File,"r") as F:
#   a = F.read()
# print(a)
##Calender
# import calendar  
# print(calendar.month(25,6))

