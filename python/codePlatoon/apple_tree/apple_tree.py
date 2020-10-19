class AppleTree:
    def __init__(self,age = 0,height = 0):
        self.age = age
        self.height = height
        self.dead = False

    def age_tree(self):
        self.age += 1
        if self.age >= 100:
            self.dead = True
    def is_dead(self):
        return self.dead
    
    def any_apples(self):
        pass

    def pick_an_apple(self):
        raise Exception('No apples on your tree')
        # Read the tests before coding.