class Pizza:

    def __init__(self):
        self.size = 1
        self.style = ""
        self.toppings = []
    
    def add_topping(self, topping):
        self.toppings.append(topping)
    
    def print_order(self):
        order = f'I would like a {self.size}-inch, {self.style.lower()} pizza with '
        for topping in self.toppings:
            order += f'{topping.lower()}, '
        else:
            order = order[slice(-2)] + f'.'
        print(order)
    

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.add_topping("Onions")
meat_lovers.print_order()
    
    
    
    
    
    
    
    
    
    
    
