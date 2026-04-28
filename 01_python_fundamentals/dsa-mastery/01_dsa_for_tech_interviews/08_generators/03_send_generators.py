def chai_customer():
    print("Welcome! What chai would you like?")
    order yield
    while True:
        print(f"Preparing: {order}")
        order = yield
stall = chai_customer()
next(stall)#start of the generator

stall.send("Lemon tea")
stall.send("Masala chai")