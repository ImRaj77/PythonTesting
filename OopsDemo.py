from docutils.parsers.rst.directives.misc import Class

# self keyword is mandatory for calling variable names into method
# class variables and instance variables are altogether have different purpose
# constructor name should be __init__
# new keyword is not required while creating an object

class Calculator:
    num = 100                   # Class Variables
    # default constructor
    def __init__(self,a,b):
        self.first_number = a
        self.second_number = b
        print("Called Automatically on object creation")

    def get_data(self):
        print("I am executing as Method in class")

    def summation(self):
        return self.first_number + self.second_number + self.num
        # return self.first_number + self.second_number + Calculator.num

obj = Calculator(2,3)              # Syntax to create Object
obj.get_data()
print(obj.num)
print(obj.summation())

obj1 = Calculator(12,13)
print(obj1.summation())
