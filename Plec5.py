class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def changeR(self, new_radius):
        self.radius = new_radius

    def findVolume(self):
        volume = (4/3) * pi * (self.radius ** 3)
        return volume

    def findArea(self):
        area = 4 * pi * (self.radius ** 2)
        return area

    def __str__(self):
        return f"Radius = {self.radius}\nVolume = {self.findVolume()}\nArea = {self.findArea()}"+'\n'

    def getattribute(self):
        return dir


pi = 3.14159265853
r1, r2 = input("Enter r1 r2 : ").split()
sphere1 = Sphere(int(r1))
print(type(sphere1))
print(sphere1.getattribute())
print(sphere1)
sphere1.changeR(int(r2))
print(sphere1)
