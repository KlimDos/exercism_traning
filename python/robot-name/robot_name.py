import random
import string
import pickle

class Robot:
    def __init__(self):
        self.name = self.__name_gen()
    def __name_gen(self):
        self.name = "".join(random.choices(string.ascii_uppercase, k=2)) + "".join(random.choices(string.digits, k=3))
        return self.name

    def reset(self):
        self.__name_gen()

r = Robot()
name = r.name
print(name)
r.reset()
name = r.name
print(name)
