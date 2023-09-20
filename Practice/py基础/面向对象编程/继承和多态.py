class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


a = list()
b = Animal()
c = Dog()
# print(isinstance(a, list))
# print(isinstance(b, Animal))
# print(isinstance(c, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


print(run_twice(Tortoise()))

