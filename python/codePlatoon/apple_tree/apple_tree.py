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
            self.apples.extend((Apple(),Apple())) # grow two apples each year
            self.has_apples = True if self.apples else False # has apples starting at age 20 and apples list is not empty
            if self.age > 100: # die at age 100
                self.dead = True


    def is_dead(self):
        return self.dead
    
    def any_apples(self):
        return True if self.has_apples else False

    def pick_an_apple(self):
        if self.any_apples():
            return self.apples.pop(random.randrange(len(self.apples)))
        else:
            raise Exception('No apples on your tree')
        
