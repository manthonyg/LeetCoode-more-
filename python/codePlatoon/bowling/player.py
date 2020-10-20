from frame import Frame
import functools
class Player:
    def __init__(self,name):
        self.name = name
        self.frame_list = [Frame() for i in range(10)]
        self.base_score = 0
        self.bonus_score = 0
    def current_score(self):
        # return functools.reduce(lambda x,y: x.total_score + y.total_score, self.frame_list)
        for i, frame in enumerate(self.frame_list):
            if i == 9:
                 break
            self.base_score += frame.total_score
            if frame.strike:
                print(f"frame {i} strike")
                self.bonus_score += self.frame_list[i + 1].total_score
            elif frame.spare:
                print(f"frame {i} spare")
                self.bonus_score += self.frame_list[i + 1].scores[0]
        print('bonus score', self.bonus_score, 'base score', self.base_score)
        return self.base_score + self.bonus_score



yang = Player('Yang')
michael = Player('Michael')


for i in range(10):
    print('*************************')
    print(f'this is {i}th frame')
    yang.frame_list[i].throw()
    # print(f'{i}th frame,throw 1, player current score',yang.current_score())
    yang.frame_list[i].throw()
    # print(f'{i}th frame throw 2, player current score',yang.current_score())

print('**********************')    # <-- I like this lolll!
print(yang.current_score())