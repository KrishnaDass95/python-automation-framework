# class variables or class attributes are values that are common to all the instances. It's not instance specific

class Employee:

    raise_amount = 1.5 # 50 % raise
    num_of_emps = 0 # class variable

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        Employee.num_of_emps += 1  # keeps a track of number of times an object has been created

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) # using a class variable can be done using class name or with self(instance) because the instance also has access to the class variables


emp_1 = Employee("kd", "dass", 500)
emp_1.apply_raise()
print(emp_1.pay)
