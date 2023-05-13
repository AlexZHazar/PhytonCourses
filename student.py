from random import randint

class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def change_name(self, new_name):
        self.name = new_name
    
    def get_avg_mark(self):
        return randint(0, 5)
