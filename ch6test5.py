class Shape:                                #Create a class
    def __init__(self, name, color):        #Initialize objects of that class
        self.name=name
        self.color=color
    def area(self,a,b,c):                   #Area function to find area
        s=(a+b+c)/2                         #Find Semiparameter
        area=(s*(s-a)*(s-b)*(s-c))**0.5     #Calculate the area
        if area%1==0:                       #Check the integer or float
            area=int(area)
        else:                               #If it is float
            area=f'{area:.3f}'              #Take three decimal places
        return area
    def perimeter(self):                    #Function to find perimeter
        p=a+b+c                             #Equation for perimeter
        return p
    def __str__(self):
        pass                                #We don't need to print it actually, so I pass it
    
class Triangle(Shape):                      #Class: Triangle inherits the Shape class
    def __init__(self, name=None, color=None, a=0, b=0, c=0):   #Initialize objects of that class
        super().__init__(name,color)        #Use super() to  call __init__ method in a parent class from a subclass
        try:                                #Use try:except: function to convert string to integer or float
            self.a=int(a)
            self.b=int(b)
            self.c=int(c)
        except:
            self.a=float(a)
            self.b=float(b)
            self.c=float(c)
            if self.a%1==0:                 #Check the float that can be changed into int
                self.a=int(self.a)
            if self.b%1==0:
                self.b=int(self.b)
            if self.c%1==0:
                self.c=int(self.c)
    def is_equilateral(self):               #Checking equilateral
        return (self.a==self.b==self.c)
    def is_isosceles(self):                 #Checking isosceles
        return (self.a==self.b or self.b==self.c or self.a==self.c)
    def is_right(self):                     #Checking right triangle
        return (self.a+1==self.b and self.b+1==self.c)
    def is_scalene(self):                   #Checking scalene
        return (self.a!=self.b and self.b!=self.c and self.a!=self.c) and Triangle.is_right(self) is False
    def getType(self):                      #Check the type of triangle according to the above functions
        if Triangle.is_equilateral(self):
            return 'an equilateral'
        elif Triangle.is_isosceles(self):
            return 'an isosceles'
        elif Triangle.is_right(self):
            return 'a right triangle'
        elif Triangle.is_scalene(self):
            return 'a scalene'
    def __str__(self):                      #Printing Method
        if isinstance(self.a,int) and isinstance(self.b,int) and isinstance(self.c,int):    
            #If the lengths are integers, I just need to print formally according to the task cases
            return f'{self.a}, {self.b} and {self.c} is {self.getType()} and area is {self.area(self.a,self.b,self.c)}.'
        else:
            #If there are some lengths that can be floats, I need to print its length just like this "7.500" 
            #So find the float one and take three decimal places for that one
            if isinstance(self.a,float):
                return f'{self.a:.3f}, {self.b} and {self.c} is {self.getType()} and area is {self.area(self.a,self.b,self.c)}.'
            elif isinstance(self.b,float):
                return f'{self.a}, {self.b:.3f} and {self.c} is {self.getType()} and area is {self.area(self.a,self.b,self.c)}.'
            elif isinstance(self.c,float):
                return f'{self.a}, {self.b} and {self.c:.3f} is {self.getType()} and area is {self.area(self.a,self.b,self.c)}.'
print(" *** Triangle ***")
inStr = input("Enter name color a b c : ")
name,color,a,b,c = inStr.split()
triangle = Triangle(name,color,a,b,c)
print(triangle)
print(f"Equilateral => {triangle.is_equilateral()}")
print(f"Isosceles   => {triangle.is_isosceles()}")
print(f"Scalene     => {triangle.is_scalene()}")
print(f"Right       => {triangle.is_right()}")