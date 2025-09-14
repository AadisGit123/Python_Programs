#Reading Files: .txt,. json, .csv

# #                                                                    .TXT
#import os
# file_path = "output.txt"

# try:
#   with open(file_path, "r") as file:
#     content = file.read()
#     print(content)
#     print(f"txt file '{file_path}' was read")
# except FileExistsError:
#   print("That file already exists")

##
# #                                                                    .JSON
# import json
# file_path = "output.json"

# try:
#   with open(file_path, "r") as file:
#     content = json.load(file)
#     print(content)#print(content["Name"/"Job"/"Age"])
#     print(f"json file '{file_path}' was read")
# except FileExistsError:
#   print("That file already exists")

#                                                       
#                                                                     BAD

# import json
# file_path = "output.json"

# try:
#   with open(file_path, "r") as file:
#     for row in file:
#      content = file.read()
#      print(content)
#     print(f"json file '{file_path}' was read")
# except FileExistsError:
#   print("That file already exists")
  
##
#                                                                     .CSV
# import csv
# file_path = "output.csv"

# try:
#   with open(file_path, "r") as file:
#     content = csv.reader(file)
#     for line in content:
#      print(line)#line[0/1/2]
#     print(f"csv file '{file_path}' was read")
# except FileExistsError:
#   print("That file already exists")
  
#                                                                     OR
#                                                                     BAD
# import csv
# file_path = "output.csv"

# try:
#   with open(file_path, "r", newline="") as file:
#     for line in file:
#      content = file.read()
#      print(content)
#     print(f"csv file '{file_path}' was read")
# except FileExistsError:
#   print("That file already exists")