# inheritence is basically having your subclass get access to all the attributes and methods of a parent class

class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    def apply_raise(self):
        self.pay *= self.raise_amt

    def full_name(self):
        return self.first + " " + self.last

    
class Developer(Employee):
    raise_amt = 1.50 # if the Dev class had a raise_amt class attribute, it will take it from the Developer class instead of the Employee class

    # now when you intantiatinte the developer class, you want to initialise its own attributes(like programming langs) along with the other attributes from parent class
    # You need to use the super class, this is how you'd do it

    def __init__(self, first, last, pay, prog_langs):
        super().__init__(first, last, pay) # use the super function to call parent constructor
        # let the parent constructor handle initilising first, last and pay attributes

        # the extra attributes that need to be initialised can be done by the Developer class
        self.prog_langs = prog_langs


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    # add new employee, remove employee and list out all the employees working for this manager
    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def removeEmployee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def list_all_employees(self):
        for emp in self.employees:
            print("----> " + emp.full_name())


# very helpful built in python function to get visibility of what happens under the hood of a class
# print(help(dev_1)) 

dev_1 = Developer("Krishna", "Dass", 100, "Python")
dev_2 = Developer("Ash", "SV", 500, "Java")
print(dev_1.email) # Krishna.Dass@company.com
print("-----")
print(dev_1.pay) # you can use the parent attributes 
dev_1.apply_raise() # you can use the parent methods directly
print(dev_1.pay)


# manager instance
# ankita_employees = ["Krishna", "Ash", "asst"]
manager_1 = Manager("Anko", "jamz", 150, [dev_1]) 
manager_1.list_all_employees()


manager_2 = Manager("Girija", "Raj", 1000)
manager_2.addEmployee(dev_1)
manager_2.addEmployee(dev_2)

print("lalalallalal")
manager_2.list_all_employees()



# testing 
# 1. You can check if an object is an instance of a class
print(isinstance(manager_1, Employee)) # True
print(isinstance(dev_1, Manager)) # False
# 2. You can check if a class is a subclass of another class
print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False