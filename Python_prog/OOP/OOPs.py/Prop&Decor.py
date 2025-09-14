# class Rectangle:
#   def __init__(self, width, height):
#               #⬆️_____⬆️______⬆️_______=>Attributes       
#     self._width = width#Private attributes
#     self._height = height
#     """@Property: lets you use methods as attributes"""
#   @property
#   def width(self):#Methods
#     return f"{self._width:.1f} cm"
  
#   @property
#   def height(self):
#     return f"{self._height:.1f} cm"
      
#   @width.setter
#   def width(self, new_width):#Parrameter
#     if new_width > 0:
#       self._width = new_width
#     else:
#       print("Width must be greater than zero")
      
#   @height.setter
#   def  height(self, new_height):#Parrameter
#     if new_height > 0:
#       self._height = new_height
#     else:
#       print("Height must be greater th an zero")
      
#   @width.deleter
#   def width(self):
#    del self._width
#    print()
#    print(f"Width has been deleted")
         
#   @height.deleter
#   def height(self):
#     del self._height
#     print(f"Height whas been deleted")

# rectangle = Rectangle(3,4)
#   #⬆️______=> Object/instance
# rectangle.width = 5
# rectangle.height = 6

# del rectangle.width
# del rectangle.height

# # print(rectangle.width)
# # print(rectangle.height)


##
# def get_him(func):
#   def song():
#     print("This looks like",end="")
#     func()
#   return song

# def follow_me(func):
#   def song():
#     print("a job for me.")
#     func()
#   return song

# @get_him
# @follow_me
# def eminm():
#   print("So, everybody follow me.")

  
# eminm()

##Decorators

# def add_sprinkles(func):
#   def wrapper(*args, **kwargs):
#     print("*You add sprinkles 🎊*")
#     func(*args, **kwargs)
#   return wrapper

# def add_fudge(func):
#   def wrapper(*args, **kwargs):
#     print("*You add fudge 🍫*")
#     func(*args, **kwargs)
#   return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavor):
#   print(f"Here is your {flavor} ice cream 🍨")
  
# get_ice_cream("Black Current")
