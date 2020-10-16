def to_roman(num):
    numerals = ["M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX", "V", "IV", "I"]
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i = 0
    while num > 0:
        if num >= values[i]:
            result = result + numerals[i]
            num = num - values[i]
        else:
            i += 1
    return result

# STRETCH GOAL - ROMAN NUMERALS AS A CLASS OBJECT
# 1. Make RomanNumerals into a Class Object
  # - Think about what data you should initialize in the __init__ method.
# 2. How many of each roman numerals exist when given an input integer
# class RomanNumerals:
# ----- Example --------
# roman_test = RomanNumerals(943)
# roman_test.find_answer()
# ==== "There are is 1 CM roman numeral, 1 XL roman numeral, and 3 I roman numerals."

from collections import OrderedDict
class RomanNumerals:

    def __init__(self,num):
        self.value = num
        self.analyze(num)
        print(self.composition)

    def analyze(self,num):
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
        for k,v in self.composition.items():
            print(f'{v} {k}') 


number = RomanNumerals(3724)
number.find_answer()
