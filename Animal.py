
def dog(): # Function
    pass

# 1. Class Defination

class Animal:
    #1.Property

    #2.Constructor

    #3.Method
    def eat(abc): # Method
        print('Hello from eat method')
    
    def sleep(abc): # Method
        print("Hello from sleep method")

#2. Class Instatiation
# We need to create object of the class

myobj = Animal()

# Now you can access the members of the class

myobj.eat() # Calling the eat method using object



# 1. Class Defination

class Dog(Animal):
    #1. Property

    #2. Constructor
    def __init__(abc):
        print('Hello from Dog init method')

    #3. Method
    def bark(abc): # method
        print("Bhow Bhow")

#2. Create the object from the Dog  class

mydog = Dog()
mydog.bark() # 

mydog.eat()