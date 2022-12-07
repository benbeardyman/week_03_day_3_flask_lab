from models.order import *


order1 = Order("Jack", "04/10/22", "Dwayne", 5)
order2 = Order("Fraser", "06/11/22", "Hubert", 20)
order3 = Order("Alex", "02/11/22", "Dwayne", 7)
orders = [order1, order2, order3]

# Dan's magic medicine:
# orders = [order1.whole_order(), order2.whole_order(), order3.whole_order()]
