class Coordinate:                               #Create a class
    def __init__(self, x, y):                   #Initialize objects of that class
        self.x=int(x)
        self.y=int(y)
    
    def __str__(self):                          #Printing method
        return f"({self.x}, {self.y})"          #Print formally

class Vector(Coordinate):                       #Class: Vector inherits the class: Coordinate
    def __init__(self, x, y):                   #Initialize objects of that class
        super().__init__(x, y)                  #use super() to  call __init__ method in a parent class from a subclass
    
    def __str__(self):                          #Printing method
        return f"({self.x}, {self.y})"          #Print formally

    def magnitude(self):                        #A function to calculate the magnitude
        mag = ((self.x)**2+(self.y)**2)**0.5    #Calculation for magnitude
        check=mag%1                             #Check the integer or float
        if check!=0:                            #If not change it to float
            mag=f'{mag:.3f}'                    #Take three decimal places
        else:                                   #if the decimal number is 0, it need to change to int
            mag=int(mag)                        #change to int
        return mag                              
    
    def __add__(self,other):                    #add method to sum
        return Vector(self.x+other.x,self.y+other.y)        #It is a given code
    
print(" *** Vector class ****")
co1,co2 = input("Enter x1 y1 / x2 y2 : ").split("/")
# print(f"co1={co1}  co2={co2}")
x1,y1 = co1.split()
x2,y2 = co2.split()
v1 = Vector(x1,y1)
v2 = Vector(x2,y2)
print(f"Vector1 = {v1}, Magnitude = {v1.magnitude()}")
print(f"Vector2 = {v2}, Magnitude = {v2.magnitude()}")
v3 = v1 + v2
print(f"V1 + v2 = {v3}, Magnitude = {v3.magnitude()}")