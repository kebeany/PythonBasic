class Dog:
    name = "coa coa"
    age = 2

    def bark(self):
        print('woof woof')

    
    def move(self):
        print('moving')

dog1=Dog()

class Dog:
    name = "coa coa"
    age = 2

    def bark(self):
        print('woof woof')

    
    def move(self):
        print('moving')

dog1=Dog()
print(dog1.name)
print(dog1.age)
dog1.bark()
dog1.move()


class Dog:
    name = "coa coa"
    age = 2

    def bark(self):
        print('woof woof')

    
    def move(self):
        print('moving')

dog1=Dog()
print(dog1.name)
print(dog1.age)
dog1.bark()
dog1.move()

dog2=Dog()
print(dog2.name)
print(dog2.age)
dog2.bark()
dog2.move()

class Dog:
  
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
    def bark(self):
        print('woof woof')

    
    def move(self):
        print('moving')

dog1 = Dog ('coa coa', 2)
dog2 = Dog ('bowow', 4)
dog3 = Dog ('dory',5)
print(dog1.name, dog1.age)
print(dog2.name,dog2.age)
print(dog3.name,dog3.age)

class Dog:
  
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    
    def bark(self):
        print('{} : woof woof'.format(self.name))

    
    def move(self):
        print('moving')

dog1 = Dog ('coa coa', 2)
dog2 = Dog ('bowow', 4)
dog3 = Dog ('dory',5)
print(dog1.name, dog1.age)
print(dog2.name,dog2.age)
print(dog3.name,dog3.age)

dog1.bark()
dog2.bark()
dog3.bark()

class Dog:
    def __init__(self,name, age, color):
        self.name = name
        self.age = age
        self.color = color
    
    def __str__(self):
        sentence = 'name :{} , age :{}, color :{}'.format(self.name, self.age, self.color)
        return sentence
    
    def bark(self):
        print('woof woof')
    def move(self):
        print('moving')

dog1 = Dog ('coa coa', 2, 'brown')
dog2 = Dog ('bowow', 4, 'black')
dog3 = Dog ('dory',5, 'white')
print(dog1.name, dog1.age)
print(dog2.name,dog2.age)
print(dog3.name,dog3.age)

dog1.bark()
dog2.bark()
dog3.bark()
print(dog1)
print(dog2)
print(dog3)
