
class PhoneBook:
    def __init__(self):
        self.numbers = {}  #Dictionary

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def get_names(self):
        pass

    def get_numbers(self):
        pass
