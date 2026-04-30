class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai()

lemon_tea = ChaiTime()
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
print(type(lemon_tea) is ChaiTime)