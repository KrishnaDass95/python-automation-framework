# class methods are methods bound to class like class variables 
# they are not bound to instances

# static methods are methods that mostly have nothing to do with anything with the class except when it has some logical connection to the class

class Employee:

    raise_amt = 1.5 # 50 % raise
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    @classmethod # use the clasmethod decorator
    def setRaiseAmt(cls, amount): # since you are using class variable and not instance, you need to pass cls as the first argument
        cls.raise_amt = amount

    # class methods can also be used as an alternative constructor
    @classmethod
    def from_string(cls, input_string):
        first, last, pay = input_string.split("-") # destructuring
        return cls(first, last, pay) # we're returning an object
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
            
    def applyRaise(self):
        self.pay *= Employee.raise_amt 
        return self.pay
        
emp_1 = Employee("Krishna", "Dass", 100)
print(emp_1.applyRaise()) # 150

Employee.setRaiseAmt(2.0)
print(Employee.raise_amt) # 2.0


# using class methods as alternative constructors
# lets say we want to make employee objects from an input string we need to parse
emp_str_1 = "ash-sv-200"
emp_str_2 = "tush-nay-400"

# take this string and form a new object with employee
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)