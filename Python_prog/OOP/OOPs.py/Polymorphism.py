# #Inheritance


# from abc import ABC, abstractmethod

# class Shape:

#   @abstractmethod
#   def area(self):
#     pass

# class Circle(Shape):
#   def __init__(self, radius):
#     self.radius = radius

#   def area(self):
#     return 3.14 *self.radius*self.radius

# class Square(Shape):
#   def __init__(self, side):
#     self.side = side

#   def area(self):
#     return self.side*self.side

# class Triangle:
#   def __init__(self, side, height):
#     self.side = side
#     self.height = height

#   def area(self):
#     return self.side*self.height*0.5
  
# class Pizza(Circle):
#   def __init__(self, topping, radius):
#     super().__init__(radius)
#     self.topping = topping
  

# shapes = [Circle(4), Square(6),   Triangle(8,9), Pizza("Paneer",21)]

# for shape in shapes:
#   print(f"{shape.area()}cm²")

# if __name__ == '__main':
#   main()
## #Duck Typing


# class Animal:
#   alive = True

# class Dog(Animal):
#   def speak(self):
#     print("WOOF !")

# class Cat(Animal):
#   def speak(self):
#     print("MEOW !")

# class Car:

#   alive = True

#   def speak(self):
#     print("HONK !")

# animals = [Dog(), Cat(), Car()]

# for animal in animals:
#   animal.speak()
#   print(animal.alive)
##

