import random


class Employee:

    def __init__(self, name=None, salary=None, age=None, employee_id=None):
        if name is None:
            self.name = self.generate_name()
        else:
            self.name = name
        if salary is None:
            self.salary = self.generate_salary()
        else:
            self.salary = salary
        if age is None:
            self.age = self.generate_age()
        else:
            self.age = age
        if employee_id is None:
            self.employee_id = None
        else:
            self.employee_id = employee_id

    @staticmethod
    def generate_name():
        count = random.randint(8, 12)
        list_of_letters = random.sample('abcdefghijklmnopqrstuvwxyz', count)
        concatenated_letters = ''.join(list_of_letters)
        name = concatenated_letters[0].upper() + concatenated_letters[1:]
        return name

    @staticmethod
    def generate_salary():
        salary = random.randrange(40, 200, 5) * 1000
        return str(salary)

    @staticmethod
    def generate_age():
        age = random.randint(18, 99)
        return str(age)

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def get_age(self):
        return self.age

    def get_employee_id(self):
        return self.employee_id

    def set_employee_id(self, employee_id):
        self.employee_id = employee_id
