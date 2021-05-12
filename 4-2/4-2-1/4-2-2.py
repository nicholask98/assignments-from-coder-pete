class Animal:
    def __init__(self):
        print('An animal has been born.')

    def eat(self):
        print('Munch munch')

    def makeNoise(self):
        print('Grrr')


class Cat(Animal):
    def makeNoise(self):
        print('Meow')


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('A dog has been born.')

    def makeNoise(self):
        print('Bark')


def main():
    # create instances of the classes
    cat = Cat()
    dog = Dog()
    animal = Animal()

    # call methods for each instance
    cat.eat()
    cat.makeNoise()
    dog.eat()
    dog.makeNoise()
    animal.eat()
    animal.makeNoise()





if __name__ == '__main__':
    main()