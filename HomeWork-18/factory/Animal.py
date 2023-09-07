__all__ = ["Animal"]


class Animal:
    def __init__(self, weight, height, pet):
        self.weight = weight
        self.height = height
        self.pet = pet

    def move(self):
        print("I am moving")