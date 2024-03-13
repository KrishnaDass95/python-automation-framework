# special methods in python help with changing the default behaviour of python in certain instances. Also called as dunder methods
# they start with double underscore __ , __init__ is the first most common special method we work with, that gets called when objects are created

# repr is an unambigious representation of the object, should be used for debugging and logging, its for other developers
# str is readable representation of the object

# repr -> when you print a random object, it always shows the memory location, but you can make it give more info

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.io'
    
    def apply_raise(self, amount):
        self.pay *= amount

    def fullname(self) -> str:
        return self.first + " " + self.last

    def __repr__(self) -> str:
        return f"Employee({self.first}, {self.last}, {self.pay})"
    
    def __str__(self):
        return f"Employee({self.fullname()} ---> {self.email})"
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

    
emp_1 = Employee("Kd", "dass", 200)
emp_2 = Employee("anko", "jamz", 500)
print(emp_1) # <__main__.Employee object at 0x103014a90> normally but with repr -> Employee(Kd, dass, 200) if you have str, it overrides - Employee(Kddass ---> Kd.dass@company.io)

# you can also call the functions using
print(emp_1.__repr__()) # Employee(Kd, dass, 200)
print(emp_1.__str__()) # Employee(Kd dass ---> Kd.dass@company.io)

# you can use the magic methods in a class to change the default behaviour of in-built function of python
print(emp_1 + emp_2) # 700 -> changes the add icon to 

print(len(emp_1)) # 7 -> We've changed the default behaviour of the object