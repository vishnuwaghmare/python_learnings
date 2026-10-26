def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Masala", "Full Cream", "2 spoons") # Positional arguments
make_chai(milk="Skimmed", tea="Ginger", sugar="1 spoon") # Keyword arguments

# arguments and keyward argumetns

def special_chai(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs) 

special_chai("Masala", "Full Cream", "2 spoons", flavor="Cardamom", size="Large")

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order() # ['Masala']
# chai_order() # ['Masala', 'Masala']

def chai_order(order=None):
    if order is None:
        order = []
    # order.append("Masala")
    print(order)

chai_order() # ['Masala']
chai_order() # ['Masala']   

