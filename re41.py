# study the given code and modify the class sphere as required.
# There is only one instance attribute named "radius".
# constructor(__init__) and changeR methods have two parameters.
# The others will have only one parameter

class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def changeR(self,new):
        self.radius=new
    def findVolume(self):
        return (4/3)*pi*self.radius**3
    def findArea(self):
        return 4*pi*self.radius**2
    def __str__(self):
        return f'Volume= {self.findVolume():0.6f} Area= {self.findArea():0.2f}'
    def getattribute(self):
        lists=[]
        for i in dir(self):
            if i[0:2]!='__':
                lists.append(i)
        return lists

pi = 3.14159265853
r1, r2 = input("Enter r1 r2 : ").split()
sphere1 = Sphere(int(r1))
print(type(sphere1))
print(sphere1.getattribute())
print(sphere1)
sphere1.changeR(int(r2))
print(sphere1)