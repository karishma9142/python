class Mammel:
    def walk(self) :
        print('walk')

class Dog(Mammel):
    def bark(self):
        print('dog is barking')

class Cat(Mammel):   
    def meow(self):
        print('cat is meowing')      

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.meow()