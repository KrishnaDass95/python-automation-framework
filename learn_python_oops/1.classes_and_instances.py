# Group data and functions to be re-used again logically
# methods - functions associated with a class 
# attributes - data of a class or variables of a class

# we make classes to model objects to use, its a blueprint of an object

class Dog:
    pass

# instance variables are variables of a particular instance
dog1 = Dog() # this is an instance
dog2 = Dog() # this is an instance
dog1.name = "Billy" # this is an  unique attribute of the instance
dog2.name = "Flash" # this is an unique attribute of the instance

print(dog1.name)
print(dog2.name)
# the name is an instance attribute

 # the above makes attributes after creating class, but you can create these attributes as you create an instance

class Employee:
    def __init__(self, first, last, pay): # self refers to the object itself
        self.first = first  # all we are saying here is new_instance.first = first -> makes so much sense now
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@' + 'companyName.com'

    def fullname(self): # make sure the methods inside classes have self as the first argument, when you call a method from an instance, it passes the self/object to the method
        return self.first + " " + self.last # in classes, to use its attributes, always use the self keyword. It helps
    

# create and initialise objects in one line

emp_1 = Employee("Krisna", "dass", 2000)
emp_2 = Employee("Anko", "Jam", 3030303)

# first, last, email and pay are all attributes of the class
print(emp_1.first)
print(emp_2.fullname())
