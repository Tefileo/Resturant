#

class Order():
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.status = 'Open'

    def add_items_order(self, item):
        self.items.append(item)

    # have a method to calculate total

    # have a method to pay,