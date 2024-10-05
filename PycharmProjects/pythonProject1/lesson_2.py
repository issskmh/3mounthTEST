# Hi Sensei
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born')

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong age. It must be an positive integer')

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def info(self):
        return f'Name: {self.__name}, Age: {self.__age}, Birth Year: {2024 - self.__age}'

    def voice(self):
        pass


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


class Cat(Animal):
    def __init__(self, name, age):
        # super().__init__(name, age)
        super(Cat, self).__init__(name, age)

    def voice(self):
        print('Meow')


class Dog(Animal):
    def __init__(self, name, age, commands):
        super(Dog, self).__init__(name, age)
        self.__commands = commands

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, commands):
        self.__commands = commands

    def info(self):
        return super().info() + f', Commands: {self.__commands}'

    def voice(self):
        print('Woof')


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins):
        super(FightingDog, self).__init__(name, age, commands)
        self.__wins = wins

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f', Wins: {self.__wins}'

    def voice(self):
        print('RRRRR woof')


# some_animal = Animal('Anim', 3)
# some_animal.set_age(5)
# print(some_animal.get_name())
# print(some_animal.info())

cat = Cat('Tom', 2)
# print(cat.info())

dog = Dog('Sharik', 10, 'Sit, run, bark')
dog.commands = 'Sit, run'
# print(dog.commands)
# print(dog.info())

fighting_dog = FightingDog('Reks', 1, 'Fight', 8)
# print(fighting_dog.info())

fish = Fish('Nemo', 4)

animals_list = [cat, fish, dog, fighting_dog]
for animal in animals_list:
    print(animal.info())
    animal.voice()

# End of program