#method dunder== double underscore
class Coordinate:
    __name='Cartesian'
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getXY(self):
        return self.x,self.y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, _o: object) -> bool:
        return self.x==_o.x and self.y==_o.y
    def getName():
        return Coordinate.__name
    def setName(name):
        Coordinate.__name=name
a = Coordinate(0,0)
b=Coordinate(2,3)
print(Coordinate.getName())
Coordinate.setName('KMITL')
print(Coordinate.getName())