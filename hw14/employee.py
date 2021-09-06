class Employee:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f'Employee: {self._name}, {self._age} years'
