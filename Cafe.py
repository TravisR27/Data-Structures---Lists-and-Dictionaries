# Creating a List for a Cafe Menu and Calculating the worth of stock left.

# List of items in menu Variable
menu_list = ['Tea', 'Coffee', 'Hot Chocolate', 'Latte', 'Muffin', 'Sandwich', 'Cake', 'Biscuit'] 

# This is the stock number of each product that is in stock within the Dictionary.
stock_dict = {'Tea': 20, 
              'Coffee': 35,
              'Hot Chocolate': 45,
              'Latte': 50,
              'Muffin': 55,
              'Sandwich': 60,
              'Cake': 25,
              'Biscuit': 15
              }
# This is the Price value for each item in the menu
price_value = {'Tea' : 1.99,
               'Coffee': 2.99,
               'Hot Chocolate': 3.99,
              'Latte': 3.50,
              'Muffin': 5.50,
              'Sandwich': 6.00,
              'Cake': 7.00,
              'Biscuit': 3.00
              }
total_stock = 0
# For Loop for calculating Stock worth
for item in menu_list:
    item_value = total_stock + (stock_dict['Biscuit'] * price_value['Biscuit'])
# Outputs Total Stock worth for each item from the menu
print(item_value) 

