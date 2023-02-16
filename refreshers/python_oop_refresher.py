
# Object-Oriented Programming in Python

# type() will tell us what data type the var is
# this will print out <class 'str'>
# print(type("hello"))

# creating a class

class Dog:
    # init will be used everytime you initialize a class
    # so if you create a new variable using Dog, it will use the init function
    # init will also take ANY parameter you pass in
    def __init__(self, name):
        # name needs to be stored inside of obj
        # this creates an attribute
        self.name = name # self.name does not need to match name
        print(name)

    def bark(self):
        print("bark")

    def get_name(self):
        # we can refer to self.name even if the function is not init
        print(self.name)

    # you can have multiple different functions in a class
    # a func in a class will always have self as argument
    # you can always add any other argument
    def add_one(self, x):
        return x + 1

    # we can modify attributes as well -- ex
    def change_name(self, name):
        self.name = name

# This is defining a variable that uses the class Dog

d = Dog("Spike") # Spike as a parameter for name

# we can now use the functions inside of Dog -- ex
d.bark() # this is inside of bark, but can be for the variable d

# you can add a parameter OUTSIDE a class -- ex
print(d.add_one(5)) # this returns the value 6

# Anything that uses self. can be referenced outside of the class -- EX
print(d.name)

# now if we do print get_name we will still grab the name
print(d.get_name())

d2 = Dog("Maverick")
d2.change_name("Achilles") # this now changes the attribute name

print(d2.get_name())