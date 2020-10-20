from frame import Frame
import functools
class Player:
    def __init__(self,name):
        self.name = name
        self.frame_list = [Frame() for i in range(10)]

    def current_score(self):
        # return functools.reduce(lambda x,y: x.total_score + y.total_score, self.frame_list)
        score = 0
        for frame in self.frame_list:
            score += frame.total_score
        return score
            



yang = Player('Yang')
michael = Player('Michael')


for i in range(10):
    yang.frame_list[i].throw()
    print(f'{i}th frame,throw 1, player current score',yang.current_score())
    yang.frame_list[i].throw()
    print(f'{i}th frame throw 2, player current score',yang.current_score())
