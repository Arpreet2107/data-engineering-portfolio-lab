def serve_chai():
    yield "Cup1: Masala Chai"
    yield "Cup2: Ginger Chai"
    yield "Cup3: Elaichi Chai"

stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_gen():
    yield "Cup1"
    yield "Cup2"
    yield "Cup3"
chai= get_chai_gen()
print(next(chai))
print(next(chai))