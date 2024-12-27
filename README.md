# codeacademy
                                        # KEY METHODS
a. PUBLIC ACCESS MODIFIER







b. Inheritance
   1. Parent
   2. Child

class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def print_info(self):
      print(self.name)
      print(self.age)

class Teacher(Person):
  def __init__(self, name, age, subject):
      self.subject = subject

      Person.__init__(self, name, age)


myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)

