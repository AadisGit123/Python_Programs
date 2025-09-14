#Writing File (.txt, .jason, .csv)

# txt_data = "I like paneer!"

# file_path = "output.txt"
# # with open(file = file_path , mode="w") as file: #Keyword arguments
# try:
#  with open(file_path ,"w") as file:
#    file.write(txt_data)
#    print(f"txt file '{file_path}' was created")
# except FileExistsError:
#   print("That file already exists")
  
##
#                                                      .TXT
# employees = ["Harry", "Hermonie", "Ron", "Pip"]

# file_path = "output.txt"

# try:
#  with open(file_path ,"w") as file:
#    for employee in employees:
#     file.write(employee + " ")
#    print(f"txt file '{file_path}' was created")
# except FileExistsError:
#   print("That file already exists")

##
#                                                       .JASON
# import json

# employee = {
#     "Name": "Catline", 
#     "Age": 28,
#     "Job": "Scientist"
#   }

# file_path = "output.json"

# try:
#   with open(file_path ,"w") as file:
#     json.dump(employee, file, indent=4)
#     print(f"json file '{file_path}' was created")
# except FileExistsError:
#   print("That file already exists")

##
#                                                       .CSV

import json
import csv

employees = [["Name", "Age", "Job"],
            ["Harry", 18, "Wizard"],
            ["Pip", 19, "Detective"],
            ["Henry", 15, "Menace"]]

file_path = "output.csv"

try:
  with open(file_path ,"w", newline="") as file:
    writer=csv.writer(file)
    for row in employees:
      writer.writerow(row)
    print(f"csv file '{file_path}' was created")
except FileExistsError:
  print("That file already exists")



  
  
  
  