class Sphere:                           #Create the class
    def __init__(self, radius):         #Constructer for 1variable
        self.radius = radius            

    def changeR(self, new_radius):
        self.radius = new_radius        #Change r1 to r2

    def findVolume(self):               
        volume = (4/3) * pi * (self.radius ** 3)        #Calculation for volume
        return f'{volume:0.6f}' 

    def findArea(self):
        area = 4 * pi * (self.radius ** 2)              #Calculation for Area
        return f'{area:0.2f}'

    def __str__(self):
        return f"Radius = {self.radius}\nVolume = {self.findVolume()}\nArea = {self.findArea()}"+'\n' #Printing formally

    def getattribute(self):
        new=[]
        for i in dir(self):
            if i[0:2]!='__':
                new.append(i)
        return new


pi = 3.14159265853
r1, r2 = input("Enter r1 r2 : ").split()
sphere1 = Sphere(int(r1))
print(type(sphere1))
print(sphere1.getattribute())
print(sphere1)
sphere1.changeR(int(r2))
print(sphere1)