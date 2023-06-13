class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name


class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal):
        '''
            Adds an animal to the appropriate queue based on its species.

    Args:
        animal (Animal): The animal object to be enqueued.

    Returns:
        None
        '''

        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue(self, pref):
        '''
          Removes and returns an animal from the specified preference queue.

    Args:
        pref (str): The preferred animal species to dequeue. Can be either "dog" or "cat".

    Returns:
        Animal or None: The animal object dequeued from the specified queue, or None if the queue is empty or an invalid preference is given.
        '''
        if pref == "dog":
            return self.dog_queue.pop(0) if self.dog_queue else None
        elif pref == "cat":
            return self.cat_queue.pop(0) if self.cat_queue else None
        else:
            return None
        


if __name__=='__main__':
 pass