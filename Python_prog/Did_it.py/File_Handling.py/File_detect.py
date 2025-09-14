import os

file_path = "output.txt" #Relative file path
#file_path = "/Users/aadityachaurasiya/Desktop/test" #Absolute file path

if os.path.exists(file_path):
  print(f"The location '{file_path}' exists")
  
  if os.path.isfile(file_path):
    print("That's a file")
  elif os.path.isdir(file_path):
    print("It's a directory")
else:
  print("That location doesn't exist")