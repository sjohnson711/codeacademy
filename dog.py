# class Dog:
#    def __init__(self, kind, age):
#       self.kind = kind
#       self.age = age

#    def owner(self):
#       print(f'The owner of the {d.kind} name is Seth Johnson, his wife Diana wants another puppy no matter if they are {d.age}, but Seth wants a {d2.kind}')

#    def wife(self, x):
#       return (x * 5) + 1

   
       
# d = Dog('golden doodle', 15)
# print(d.kind, d.age)


# d2 = Dog('puppy', 17)
# print(d2.kind, d2.age)


# d.owner()

# print(d.wife(20))

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('"You have come to a lake, which way do you want to go? "left or right:').lower()


if direction == 'left':
    action = input("You've cae to an island and you can "
                   "either choose to swim or wait").lower()

    if action == 'wait':
        door = input('you have arrived at the island unharmed. There is three doors, which one? ').lower()

        if door == 'red':
            print('Room full of fire game over')
        elif door == 'yellow':
            print('you have found the treasure')
        else:
            print('room full of water. Game over')

    else:
        print('you have been attacked and killed')
else: # if choose right or anything ELSE
    print('You fell in a hole, game over')
