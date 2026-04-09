class Point:
    def move(self) :
        print('move')

    def draw(self) :
        print('draw')    

point1 = Point()
point1.draw();
point1.x=10
point1.y=12
print(point1.x)
point1.move()   