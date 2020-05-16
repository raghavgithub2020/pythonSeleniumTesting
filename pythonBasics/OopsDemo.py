# classes are user define blue print or prototypes
# clssses will have Methods, class variables, instance variables, constructors etc.


# Self key work is mandatory for calling variable name into methods
# Instance and Class variables have whole different purpose
# Constructor name should be __init__
# new keyword is NOT required when create an Object


class Calculator:
    num = 100 # classes variables

# default constructor
    def __init__(self, a, b ):
        self.firstname = a # instance variables which are declared in a method
        self.lastname = b
        print("called automatically when object is created")

    def getData(self):
        print("i m Testing")

    def summation(self):
        return self.firstname + self.lastname + Calculator.num # here you can call class variable with self.num also it is global veriable.

obj = Calculator(2, 3) # Syntax to create an object in python
obj.getData()
print(obj.summation())


obj1 = Calculator(5, 6)
obj1.getData()
print(obj1.summation())





