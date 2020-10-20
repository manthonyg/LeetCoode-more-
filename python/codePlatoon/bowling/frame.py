import random

class Frame:

    # if Frame.scores[0] + Frame.scores[1] = 10 //spare
    # if Frame.scores[0] == 10 //strike

    def __init__(self):
        self.scores = [0,0]
        self.bonus = 0
        self.spare = False
        self.strike = False
        self.num_throws = 2
        
    def spare_or_strike(self):
        if self.scores[0] == 10:
            self.strike = True
        elif sum(self.scores) == 10:
            self.spare = True
        return self.scores
    
    def throw(self):
        self.num_throws -= 1
        first_score = random.randint(0,10)
        second_throw_max_score = 10 - self.scores[0]

        if self.num_throws == 1: # first throw
            self.scores[0] = first_score
        else: # second throw
            self.scores[1] = random.randint(0, second_throw_max_score)


frame = Frame()
frame.throw()
frame.throw()
print(frame.scores)
        
        
