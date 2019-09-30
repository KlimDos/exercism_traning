class Dog:
    # ! only for good boi's
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
            "Documentation"
            strng = f'I am a dog {self.name} and I\'m {self.age}'
            return strng

def pass_the_time(age,time):
    summ = int(age) + int(time)
    return summ
