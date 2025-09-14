# class Car:
#   def __init__(self, model, year, color, for_sale):
#     self.model = model
#     self.year = year
#     self.color = color
#     self.for_sale = for_sale

#   def drive(self):
#     print(f"You Drive the {self.color} {self.model}")

#   def stop(self):
#     print(f"You stop the {self.color} {self.model}")
 
#   def describe(self):
#     print(f"{self.year} {self.model} {self.color}")

# # from car import Car

# car1 = Car("BMW", 2025, "Red", False)
# car2 = Car("Audi", 2020, "Green", True)
# car3 = Car("Charger", 2026, "White", True)

# car1.stop()
# car1.describe()
# car2.describe()
# car3.describe()
# car1.drive()
# car2.drive()
# car3.drive()

##
# class Student:

#   class_year = 2026
#   strength = 0

#   def __init__(self, name, age):
#     self.name=name
#     self.age = age
#     Student.strength += 1

# stud1=Student("Phenius",30)
# stud2=Student("Patric",35)
# stud3=Student("Saitama",28)
# stud4=Student("Sandy",29)

# print(f"My graduating class of {Student.class_year} has {Student.strength} students")
# print(stud1.name)
# print(stud2.name)
# print(stud3.name)
# print(stud4.name)

## Inheritance
# class Animal:
#   def __init__(self, name):
#     self.name = name
#     self.is_alive = True

#   def eat(self):
#     print(f"{self.name} is eating")

#   def sleep(self):
#     print(f"{self.name} is sleeping")

# class Dog(Animal):
#   def speak(self):
#     print("WOOF!")

# class Cat(Animal):
#   def speak(self):
#     print("Meow")

# class Mouse(Animal):
#   def speak(self):
#     print("SQUEEK")

# class Bird:
#   def __init__(self,speed):
#     self.speed = 50
  
# class Bat(Animal):
#   class Bat(Bird):
#    def speed(self):
#     print(f"{self.name} can fly at a speed of {self.speed}km/h")

# bat = Bat("Chad")
# dog = Dog("Scooby")
# cat = Cat("Garfield")
# mouse = Mouse("Jerry")


# print(mouse.name)
# # # print(mouse.is_alive)
# # # mouse.eat()
# # # mouse.sleep()
# mouse.speak()
# # print(bat.name)
# # bat.speed()
