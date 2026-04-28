# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing",order)

# prepare_chai(chai)
# print(chai)

chai = [1,2,3]

def edit_chai(cup):
    cup[1]= 42
edit_chai(chai)
print(chai)

def make_chai(tea,milk,sugar):
    print(tea,milk,sugar)
make_chai("Black","Yes","Low") #positional arguments
make_chai(tea="Green",sugar="Medium",milk="No")#keywords arguments

def special_chai(*ingridients,**extras):
    print("Ingridients",ingridients)
    print("Extras",extras)

special_chai("Cinnamon","Cardamom",sweetner="Honey",foam="Yes")

def chai_order(order=[]):
    order.append("Masala chai")
    print(order)
chai_order()
chai_order()

def chai_order(order=None):
    if order is None:
        order=[]
    print(order)
chai_order()
chai_order()