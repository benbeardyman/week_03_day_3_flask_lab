class Order():
    def __init__(self, customer_name, order_date, rock_name, quantity):
        self.customer_name = customer_name
        self.order_date = order_date
        self.rock_name = rock_name
        self.quantity = quantity

    # Dan's magic medicine:
    # def whole_order(self):
    #     return f"{self.customer_name}  {self.order_date} {self.rock_name} {str(self.quantity)}"
        