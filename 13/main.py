class Animal:
    def eat(self):
        print('eating')

    def move(self):
        print('moving')

class Dog(Animal):
    def bark(self):
        print('woof woof')

    def shake(self):
        print("tail wagging")

dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()

class Animal:
    def eat(self):
        print('eating')

    def move(self):
        print('moving')

class Dog(Animal):
    def __init__(self,name,age,owner):
        self.name = name
        self.age = age
        self.owner = owner
    def bark(self):
        print('woof woof')

    def shake(self):
        print("tail wagging")

dog = Dog('coco', 2 ,'bob')
print(dog.name,dog.age,dog.owner)

class Animal:
    def eat(self):
        print('eating')

    def move(self):
        print('moving')

class Dog(Animal):
    def __init__(self,name,age,owner):
        self.name = name
        self.age = age
        self.owner = owner
    def bark(self):
        print('woof woof')

    def shake(self):
        print("tail wagging")

    def __str__(self):
        sentence = 'name : {}, age : {}, owner : {}'.format(self.name,self.age,self.owner)
        return sentence

dog = Dog('coco', 2 ,'bob')
print(dog)

class Animal:
    def __init__(self,age):
        self.age = age
    def eat(self):
        print('eating')
    def move(self):
        print('moving')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(age)
        self.name = name
        self.owner = owner

    def bark(self):
        print('woof woof')

    def shake(self):
        print("tail wagging")

    def __str__(self):
        sentence = 'name : {}, age : {}, owner : {}'.format(self.name,self.age,self.owner)
        return sentence
animal = Animal(10)
dog = Dog('coco' , 2 , 'bob')
# print(animal)#error
print(dog)

class Animal:
    def __init__(self, age):
        self.age = age
    def eat(self):
        print('eating')
    def move(self):
        print('moving')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(age)
        self.name = name
        self.owner = owner

    def bark(self):
        print('woof woof')

    def shake(self):
        print("tail wagging")

    def __str__(self):
        sentence = 'name : {}, age : {}, owner : {}'.format(self.name,self.age,self.owner)
        return sentence

    def eat(self):
        print('dog is eating food')

    def move(self):
        print('dog is moving')

dog = Dog('coco' , 2 , 'bob')
print(dog)
dog.eat()
dog.move()
