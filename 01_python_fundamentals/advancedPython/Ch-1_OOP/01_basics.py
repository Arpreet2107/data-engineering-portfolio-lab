class Myclass:
    #class variables
    var1 = "Arpreet"
    var2 = "Mahala"
    #class methods
    def func1(self):
        print("Hello World")
    def func2(self):
        print("Welcome to OOPs")

#Creating an object of the class
object1 = Myclass()
object2 = Myclass()
#Accessing class variables using the object
print(object1.var1)
print(object2.var2)
#Accessing class methods using the object
object1.func1()
object2.func2()