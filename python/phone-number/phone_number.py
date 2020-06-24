class PhoneNumber:
    def __init__(self, number):
        self.input = number
        self.clean = self.__clean()
        self.number = self.__country_code()
        self.area_code = self.__area_code()

    def __clean(self):
        s = ""
        for i in self.input:
            if i.isdigit():
                s += i
        return s

    def __country_code(self):
        if len(self.clean) == 11:
            if self.clean[0] != "1":
                raise ValueError("Wrong country code")
            else:
                self.number = self.clean[1:]
        elif len(self.clean) == 10:
            self.number = self.clean
        else:
            raise ValueError("Wrong number")
        return self.number

    def __area_code(self):
        if int(self.number[0]) < 2:
            raise ValueError("Wrong area code")

        if int(self.number[3]) < 2:
            raise ValueError("Wrong exchange code")

        return self.number[0:3]

    def pretty(self):
        result = f"({self.area_code}) {self.number[3:6]}-{self.number[6:]}"
        return result
