# methos overloading

class Bird():
    def sound(self):
        print('bird make sound')

class Crow(Bird):
    def sound(self):
        print('crow say cow cow') 

class Parrot(Bird):
    def sound(self):
        print('parrot makes sound')

bird1 = Crow()
bird2=Parrot()

bird1.sound()
bird2.sound()

# operator overlading

def add(a,b):
    print(a+b)

add(2,3)
add('karishma ' , 'rawat')
add([1,2,3] , [4,5,6])    