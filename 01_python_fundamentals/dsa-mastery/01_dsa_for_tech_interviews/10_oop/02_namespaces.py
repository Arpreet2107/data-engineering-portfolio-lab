class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot=True
print(Chai.is_hot)

#creating objects from the class Chai
masala = Chai()
print(f"Masala{masala.origin}")
print(f"Masala{masala.is_hot}")

masala.is_hot = False
print("Class: ",Chai.is_hot)
print(f"Masala{masala.is_hot}")
#So here the question is if I change anything inside an object,
#should this change be propagated inside the class as well?
#-> If we run the file we will get that the program says this Masala India and True
# After that we see the class and its still True but in the masala it becomes False
# So this proves the point that each object is actually having its own namespace which
#doesn't affect other objects also doesn't affect the classes aswell.BY-DEFAULT but if we wish we can change it.
masala.flavor= "Masala"
print(masala.flavor)