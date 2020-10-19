from apple import Apple
import random

class AppleTree:
    def __init__(self,age = 0,height = 0):
        self.age = age
        self.height = height
        self.dead = False
        self.has_apples = False
        self.apples = []

    def age_tree(self):
        self.age += 1

        if self.age < 20:
            self.height += 5
        else:
            self.has_apples = True # has apples starting at age 20
            self.apples.extend((Apple(),Apple())) # grow two apples each year
            if self.age > 100: # die at age 100
                self.dead = True

    def is_dead(self):
        return self.dead
    
    def any_apples(self):
        return self.has_apples

    def pick_an_apple(self):
        if self.has_apples:
            return 
        else:
            raise Exception('No apples on your tree')
        