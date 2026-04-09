class Point:
    def __init__(self , x, y):
        self.x=x
        self.y=y

    def move(self) :
        print('move')    

ponit1 = Point(2,3)
print(ponit1.x)
ponit1.x=10
print(ponit1.x)


class Persion:
    def __init__(self , name):
        self.name=name

    def greet(self):
        print(f"hello {self.name}")  

    def talk(self) :
        print('talk')    

perion1 = Persion('karishma')
perion1.greet()
perion1.talk()        
