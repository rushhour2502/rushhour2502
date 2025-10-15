class Employee:
    raise_amount = 1.04
    def __init__(self, name, last, salary):
        self.name = name
        self.last = last
        self.salary = salary
        self.email = self.name + "@" + self.last + ".@company.com"

    def fullname(self):
        return "{} {}".format(self.name, self.last)

    def apply_raise(self):
        return self.salary * self.raise_amount


class Manager(Employee):
    def __init__(self, name, last, salary, employees= None):
        super().__init__(name, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def show_name(self):
        for emp in self.employees:
            print(emp.fullname)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Sll head is null")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                a = a.next

