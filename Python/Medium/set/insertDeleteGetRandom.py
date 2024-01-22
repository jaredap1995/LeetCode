import random
class Randomset:
    def __init__(self):
        self.this = set()

    def add(self, val):
        if val not in self.this:
            self.this.add(val)
            return True
        return False

    def remove(self, val):
        if val in self.this:
            self.this.remove(val)
            return True
        return False

    def getRandom(self):
        return random.choice(tuple(self.this))