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

























`

class Dog:
  def __init__(self, breed, age):
    self.breed = breed
    self.age = age

  def my_dog(self):
    print(f'Isha is a {self.breed}, and she is only {self.age}')

pup = Dog('golden doodle', '2 years old)
pup.my_dog()
