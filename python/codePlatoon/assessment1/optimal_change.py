from collections import OrderedDict





class ChangeMaker:
    def __init__(self,price,paid):
        self.price = price
        self.paid = paid
        self.analyze(price,paid)

    def analyze(self,price,paid):
        self.singles = ["$20 bill", "$10 bill", "$5 bill", "$1 bill", "quarter", "dime", "penny"]
        self.plurals = ["$20 bills", "$10 bills", "$5 bills", "$1 bills", "quarters", "dimes", "pennies"]
        values = [20, 10, 5, 1, float(0.25), float(0.1), float(0.01)]
        self.change_dict = OrderedDict()
        change = paid - price
        i = 0
        while change > 0:
            if change >= values[i]:
                # round() handle Floating Point Arithmetic
                change = round(change - values[i], 2)
                if self.change_dict.get(i) is not None:
                    self.change_dict[i] += 1
                else:
                    self.change_dict[i] = 1
            else:
                i += 1

    def optimal_change(self):
        string_to_print = f'The optimal change for an item that costs ${self.price} with an amount paid of ${self.paid} is '
        while bool(self.change_dict):
            index, number = self.change_dict.popitem(last=False)
            # check if reached last pair in dict
            if bool(self.change_dict):
                if number > 1:
                    string_to_print += f'{number} {self.plurals[index]}, '
                else:
                    string_to_print += f'{number} {self.singles[index]}, '
            # reached last pair in dict
            else:
                if number > 1:
                    string_to_print += f'and {number} {self.plurals[index]}.'
                else:
                    string_to_print += f' and {number} {self.singles[index]}.'

        print(string_to_print)
            



change_maker1 = ChangeMaker(62.13, 100)
change_maker1.optimal_change()
change_maker2 = ChangeMaker(31.51, 50)
change_maker2.optimal_change()
