from collections import OrderedDict


def optimal_change(num):
    singles = ["$20 bill", "$10 bill", "$5 bill", "$1 bill", "quarter", "dime","penny"]
    plurals = ["$20 bills", "$10 bills", "$5 bills", "$1 bills", "quarter", "dime","penny"]
    
    values = [20, 10, 5, 1, 0.25, 0.1, 0.01]

class ChangeMaker:
    def __init__(self,price,paid):
        self.price = price
        self.paid = paid
        self.analyze(price,paid)

    def analyze(self,price,paid):
        self.composition = OrderedDict

    def optimal_change(self):




class RomanNumerals:

    def __init__(self, num):
        self.value = num
        self.analyze(num)
        print(self.composition)

    def analyze(self, num):
        self.composition = OrderedDict()
        numerals = ["M", "CM", "D", "CD", "C", "XC",
                    "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        while num > 0:
            if num >= values[i]:
                num = num - values[i]
                if self.composition.get(numerals[i]) is not None:
                    self.composition[numerals[i]] += 1
                else:
                    self.composition[numerals[i]] = 1
            else:
                i += 1

    def find_answer(self):
        print('there are ')
        for k, v in self.composition.items():
            print(f'{v} {k}')


number = RomanNumerals(3724)
number.find_answer()
