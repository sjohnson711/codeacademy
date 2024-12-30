# # DICTIONARIES
# grocieries = {'fruits': ['mangoes', 'bananas', 'kiwis'], 
# 'protein': ['beef', 'pork', 'salmon'],
# 'carbs': ['rice', 'pasta', 'bread'],
# 'veggies': ['lettuce', 'cabbage', 'onion']}

# print(grocieries['carbs'])



# party_planning = {'Yes', 10,
#                   'No': 15,
#                   'Maybe': 30, 
#                   'Location', 'Our backyard'
#                   'Date': '2022/05/01'}

# print(party_planning('Location'))


shopping_list1 = {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 200}
shopping_list2 = {'shoes': 'sandals', 'budget': 350}
 
shopping_list1.update(shopping_list2)
 
print(shopping_list1) # prints {'jewelry': 'earrings', 'clothes': 'jeans', 'budget': 350, 'shoes': 'sandals'}