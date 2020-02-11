from people_class import People, Customer
from food_items_class import FoodItem, Combos
from order_class import Order

# We want a game to keep running
# Create a simple switch board

# We want the following options:
# As a user i can create a customer
# As a user i can create Food items
# As a user i can list food items
# As a user i can create Orders (depends on selecting a user)
# As a user i can add items to order (requires a specific order and selecting of food items)
# As a user i can see the total or an order (requires a calculating the total of all food items)

while True:
    pass
    # print option
    print('Where would you like to go? \n 1 - create a customer')
    user_input = input('>>>')

    # get user input
    if user_input == '1' or 'create customer' in user_input:

        customer_name = input('Enter Name Here >>>')
        customer_location = input('Enter Customer Location Here >>>')

        customer1 = Customer(customer_name, customer_location)

        print('I am going to create a customer')
        
    elif user_input == '2' or 'create food' in user_input:
        print('Wohoo! Let us make magic')

    # Evaluate and go to each option
        # Inside each option, do logic and create whatever you need to create