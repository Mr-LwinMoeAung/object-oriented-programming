
#method dunder== double underscore
class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getXY(self):
        return self.x,self.y
    def __str__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self, _o: object) -> bool:
        return self.x==_o.x and self.y==_o.y

a = Coordinate(0,0)
# a.x=0
# a.y=0
print(f'x={a.x} y={a.y}')
print(a.getXY())
b=Coordinate(2,3)
print(b)
print(a==b)
print(f'{id(a):08X} {id(b):08X}')
print()