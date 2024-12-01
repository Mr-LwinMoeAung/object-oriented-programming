#  *** Class Point ***
# Enter x1 y1 / x2 y2 : 1 2 / 3 4
# in1= '1 2 ' in2= ' 3 4'
# p1 = (1, 2)
# p2 = (3, 4)
# Middle point = (2, 3)
# distance = 2.828

class Point:
    def __init__(self,arg1,arg2=None):
        if arg2 is None:
            x,y=arg1.split()
            self.x=int(x)
            self.y=int(y)
        elif arg2 is not None:
            self.x=int(arg1)
            self.y=int(arg2)
        
    def __str__(self):
        return f"({self.x}, {self.y})"
    def __add__(self,other):
        return self.x+other.x,self.y+other.y
    def midPoint(self,other):
        return ((self.x+other.x)//2,(self.y+other.y)//2)
    def distance(self,other):
        ans=((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
        return f'{ans:0.3f}'

print(" *** Class Point ***")
in1,in2 = input("Enter x1 y1 / x2 y2 : ").split('/')
print(f"in1= '{in1}' in2= '{in2}'")
p1= Point(in1)
print("p1 =",p1)
p2x,p2y = in2.split()
p2 = Point(p2x,p2y)
print("p2 =",p2)
print(f"Middle point = {p1.midPoint(p2)}")
print(f"distance = {p1.distance(p2)}")