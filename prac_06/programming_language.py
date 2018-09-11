""" CP1404 Prac 06 Programming Languages Class """


class ProgrammingLanguage:
    def __init__(self, name="", typing="Static", reflection=False, year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{self.name}, {self.typing} typing, Reflection={self.reflection}, First appeared in {self.year}".format(self=self)

    def is_dynamic(self):
        if self.typing == "Static":
            return False
        elif self.typing == "Dynamic":
            return True
