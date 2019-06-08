# https://www.learnpython.org/en/Classes_and_Objects

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable)
myobjectx.function()