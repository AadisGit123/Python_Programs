# A concept of Inheritance.


# import math as mh
# class Shape:
#   def __init__(self, color, is_filled):
#     self.color = color
#     self.is_filled = is_filled

#   def describe(self):
#     print(f"It's {self.color} and is ",end="")
#     print('filled' if self.is_filled else 'not filled')

# class Circle(Shape):
#   def __init__(self, color, is_filled, radius):
#    super().__init__(color, is_filled)
#    self.radius = radius
#    self.area = mh.pi*radius*radius

#   def Area(self):
#     print(f"It's a Circle with an area of {self.area}")

# class Square(Shape):
#   def __init__(self, color, is_filled, width):
#    super().__init__(color, is_filled)
#    self.width = width
#    self.area = width*width
  
#   def Area(self):
#     print(f"This square has an area of {self.area}")

# class Triangle(Shape):
#   def __init__(self,color, is_filled, width, height):
#    super().__init__(color, is_filled)
#    self.width = width
#    self.height = height
#    self.area  = .5*height*width
  
#   def Area(self):
#     print(f"This Triangle has an area of {self.area:.2f}")

# circle = Circle(color="Red", is_filled=True, radius=5)
# square = Square(color="Blue", is_filled=True, width=10)
# triangle = Triangle(color="Green", is_filled=False, width=7, height=8)

# square.describe()

##

class Birds:
  def __init__(self, name):
    self.name = name
    self.can_fly = True
    
  def Pet(self):
    print(f"{self.name} is a pet")
    
  def Fly(self):
    print(f"{self.name} can fly")
    
class Pigeon(Birds):
  pass
    
pigeon = Pigeon("Henry")

print(pigeon.name)
pigeon.Fly()
pigeon.Pet()