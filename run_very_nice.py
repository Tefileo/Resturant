from people_class import People, Customer
from food_items_class import FoodItem, Combos
from order_class import Order

# As a resturant owner i can create new customers
customer1 = Customer('John', '21 Down Town Abi, London')
customer2 = Customer('Anabela', 'Hackney, London')
print(customer1, customer2)

# As a resturant owner i can create new food items
# 3 mains
main1 = FoodItem('Sea Bass', 17.5, ['Sea bass fish'])
main2 = FoodItem('Omelet du Formage Avec Champignon', 9, ['Egg', 'Cheese', 'Mushroom'])
main3 = FoodItem('Fiorentina', 5.50, ['Tomato Sauce', 'Mozzarella', 'Parmesan', 'Egg', 'Fresh Spinach'])
print(main1, main2, main3)

# 3 sides
side1 = FoodItem('Garlic Bread', 4, ['bread', 'garlic', 'oregano', 'cheese'])

# 3 drinks
drink1 = FoodItem('water', 2, ['water'])
drink2 = FoodItem('Cocacola', 3, ['others'])
drink3 = FoodItem('Smoothies', 4, ['orange', 'carrots', 'kiwi'])


# 3 combos!

# As a resturant owner, i can create new orders and add food item for a customer.
# opening a tab to order

order1 = Order(customer1)
order1.add_items_order(main3)
order1.add_items_order(drink3)

print(order1)
print(order1.items)
for item in order1.items:
    print(item.item, f' ${item.price}')