##Static Methods

# class Employee:
#   def __init__(self, name, position):
#     self.name = name
#     self.position = position 

#   def get_info(self):
#     print()
#     print(f"{self.name}'s designation is {self.position}")

#   @staticmethod
#   def is_valid_position(position):
#     valid_positions = ["Manager", "Cashier", "Cook", "Janator"] 
#     return position in valid_positions
  
# employee1 = Employee("Cid", "Manager")
# employee2 = Employee("Saitama", "Hero")
# employee3 = Employee("Rimuru", "Cashier")

# # print(Employee.is_valid_position("Hero"))

# employee1.get_info()
# employee2.get_info()
# employee3.get_info()
# print()

###Class Methods


# class Student:
  
#   count = 0
#   total_gpa = 0

#   def __init__(self, name, gpa):
#     self.name = name
#     self.gpa = gpa
#     Student.count += 1
#     Student.total_gpa += gpa

#   def get_info(self):
#     return f"{self.name} {self.gpa}"
  
#   @classmethod
#   def get_count(cls):
#     return f"Total # of students: {cls.count}"
  
#   @classmethod
#   def get_avg_gpa(cls):
#     if cls.count == 0:
#       return 0
#     else:
#       return f"{cls.total_gpa/cls.count:.2f}"
  
# student1 = Student("Henry", 3.8)
# student2 = Student("Coupe", 2.5)
# student3 = Student("Bob", 3.4)



# print(Student.get_count())
# print(f"Average GPA: {Student.get_avg_gpa()}")

##

# class Book:

#   def __init__(self, title, author, num_pages):
#     self.title = title
#     self.author = author
#     self.num_pages = num_pages

#   def __str__(self):
#     return f"'{self.title}' by {self.author}"  

#   def __eq__(self, other):
#     return self.title == other.title and self.author == other.author 
  
#   def __lt__(self, other):
#     return self.num_pages < other.num_pages
  
#   def __gt__(self, other):
#     return self.num_pages > other.num_pages
  
#   def __add__(self, other):
#     return self.num_pages + other.num_pages
  
#   def __contains__(self,keyword):
#     return keyword in self.title or keyword in self.author
  
#   def __getitem__(self, key):
#     if key =="title":
#       return self.title
#     elif key =="author":
#       return self.author
#     elif key =="num_pages":
#       return self.num_pages
#     else :
#       return f"Key {key} Not Found!"

# book1 = Book("Good Girl's Guide to Murder", "Holly Jackson", 433)
# book2 = Book("Harry Poter and the Deathly Hallows", "J.K. Rowling", 253)
# book3 = Book("Let Us C", "Vishwanath Kanatkar", 320)

# # print(book1)
# # print(book1 == book2)
# # print(book1 < book2)
# # print(book1 > book2)
# # print(book1 + book2)
# # print("Good" in book1)
# print(book1['title'])
# print(book2['author'])
# print(book3['num_pages'])
# print(book3['audio'])

##