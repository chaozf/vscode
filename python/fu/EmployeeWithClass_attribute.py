from EmployeeWithClass import Employee

print("Number of employee s before instantiation is",\
    Employee.count)

#creat two Employ objects
employee1 = Employee("chao", "zf")
employee2 = Employee("zhang", "san")
employee3 = employee1

print("Numeber of employees after instantiation is",\
    Employee.count)

# explicitly delete empolyee objects by removing references
del employee1
del employee2
del employee3

print("Number of employee after deletion is",\
    Employee.count)