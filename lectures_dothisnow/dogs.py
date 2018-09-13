class Dog:
    def __init__(self, breed="", age=0, sex=""):
        self.breed = breed
        self.age = age
        self.sex = sex

    def __str__(self):
        return "{} {} years {}".format(self.breed, self.age, self.sex)

