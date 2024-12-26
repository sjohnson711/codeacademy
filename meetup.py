# Public Access Modifier
# class Dog:
#     def __init__(self, breed, age):
#         self.breed = breed
#         self.age = age
#     def display_dog(self):
#         print(f'Breed: {self.breed}, Age: {self.age}')

# first = Dog('golden doodle', '2 years old') # intializing
# first.display_dog() # prints Breed: golden doole, Age: 2 years old

# class Dog:
#     def __init__(self, breed, age):
#         self._breed = breed # protected - only can be used in the class unless it is apart of a subclass
#         self._age = age # ""
#     def display_dog(self):            
#         print(f'Breed: {self._breed}, Age: {self._age}')

# first = Dog('golden doodle', '2 years old')
# first.display_dog()


# class Dog:
#     def __init__(self, breed, age):
#         self.__breed = breed # private access modifier, if trying to access outside the class will cause a attribute error
#         self.__age = age
#     def display_dog(self):
#         print(f'Breed: {self.__breed}, Age: {self.__age}')

# second = Dog('golden doodle', '2 year old')
# second.display_dog()

    





# name = 'Mary'
# password = 'Harmony1'
# name = input("What is your name? ").lower().strip().title() #ask the question about name
# password = input("password: ").lower().strip().title() # ask password
# if name == 'Mary':
#     print('Hello, Mary')

#     if password == 'Harmony1':
#         print('Access Granted')
#     else:
#         print('Access Denied')
# class Teacher:
#     def __init__(self, instructor, name):
#         self.instructor = instructor
#         self.name = name

#     def his_name(self):
#         print(f'Instructor: {self.instructor}, Name: {self.name}')


# first = Teacher('Dr. Johnson', 'Big Dog')
# first.his_name()

# second = Teacher('Dr. Robinson', 'Young Lady')
# second.his_name()



# two list with number that need to be combined but alternate starting with list A 

# InputListOne = [1, 3, 5, 7, 9]
# InputListTwo = [2, 4, 6, 8, 10]

# def Solution(InputListOne, InputListTwo):
#     a = []

#     for i in range(len(InputListOne)):
#         a.append(InputListOne[i])
#         a.append(InputListTwo[i])
#     return a 

# results = Solution(InputListOne, InputListTwo)
# print(results)





# Encaptsulation - wrapping variable and methods in one unit
# class UserInfo:
#     def __init__(self, username, email_address):
#         self.username = username
#         self.email_address = email_address

# user = UserInfo('user123', 'abc@edf.ghi')

# user.username
# user.email_address

# Encapsulation

# class UserInfo:
#     def __init__(self, username, email_address):
#         self.username = username
#         self.email_address = email_address

#     def check_username(self, username_to_check):
#         if username_to_check == self.username:
#             return True
#         else:
#             return False
#     def check_email_address(self, email_address_check):
#         if email_address_check == self.email_address:
#             return True
#         else:
#             return False
        

        
# user = UserInfo('user123', 'abc@edf.ghi')

# print(user.check_username('user123')) # returns True
# print(user.check_username('user456')) # returns False
# print(user.check_email_address('abc@edf.ghi')) # returns True
# print(user.check_email_address('seth.johnson')) # returns False







