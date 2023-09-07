from factory.Animal import Animal


class Fish(Animal):

    def __init__(self, weight: int, height: int, pet: bool, species: str):
        super().__init__(weight, height, pet)
        self.__species = species

    def move(self):
        print("I am swimming")

    def get_species(self):
        return self.__species