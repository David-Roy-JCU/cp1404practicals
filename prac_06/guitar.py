""" CP1404 prac 06 guitars!!! YASSSSSSSS!!!!! """

import datetime

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{self.name} ({self.year}) : {self.cost}".format(self=self)

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True