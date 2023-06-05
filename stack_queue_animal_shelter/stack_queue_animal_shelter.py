class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        if pref == "dog":
            return self.dog_queue.pop(0) if self.dog_queue else None
        elif pref == "cat":
            return self.cat_queue.pop(0) if self.cat_queue else None
        else:
            return None
        


if __name__=='__main__':
 