class Point:                                    #Create a class
    def __init__(self, arg1, arg2=None):        #Constructer for 2 variables
        if arg2 is not None:                    #According to the given above function   
            self.x = int(arg1)
            self.y = int(arg2)
        else:
            x, y = arg1.split()                 
            self.x = int(x)
            self.y = int(y)

    def __str__(self):
        return f"({self.x}, {self.y})"      #Printing 

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)    #Adding two X and two Y

    def midPoint(self, other):                          
        midX = (self.x + other.x) / 2                       #Calculation for midpoint
        midY = (self.y + other.y) / 2
        return Point(midX, midY)                                

    def distance(self, other):  
        ans=((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5      #Finding Distance
        return f'{ans:0.3f}'


print(" *** Class Point ***")
in1, in2 = input("Enter x1 y1 / x2 y2 : ").split('/')
print(f"in1= '{in1}' in2= '{in2}'")
p1 = Point(in1)
print("p1 =", p1)
p2x, p2y = in2.split()
p2 = Point(p2x, p2y)
print("p2 =", p2)
print(f"Middle point = {p1.midPoint(p2)}")
print(f"distance = {p1.distance(p2)}")