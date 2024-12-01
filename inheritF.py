# class A:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f'name={self.name}   age={self.age}'
# class B(A):
#     pass

# print(" *** B inherit A ***")
# name,age = input("Enter name age : ").split()
# b = B(name,age)
# print(b)





# class Coordinate:
#     def __init__(self, x, y):
#         self.x=int(x)
#         self.y=int(y)
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"

# class Vector(Coordinate):
#     def __init__(self, x, y):
#         super().__init__(x, y)       
    
#     def __str__(self):
#         return f"({self.x}, {self.y})"

#     def magnitude(self):
#         mag = (self.x**2+self.y**2)**0.5
#         return f'{mag}'
    
#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
    
# print(" *** Vector class ****")
# co1,co2 = input("Enter x1 y1 / x2 y2 : ").split("/")
# # print(f"co1={co1}  co2={co2}")
# x1,y1 = co1.split()
# x2,y2 = co2.split()
# v1 = Vector(x1,y1)
# v2 = Vector(x2,y2)
# print(f"Vector1 = {v1}, Magnitude = {v1.magnitude()}")
# print(f"Vector2 = {v2}, Magnitude = {v2.magnitude()}")
# v3 = v1 + v2
# print(f"V1 + v2 = {v3}, Magnitude = {v3.magnitude()}")


# class MyInt:
#     def __init__(self,a):
#         self.a=int(a)
#     def __str__(self):
#         return f'{self.a}'
#     def __add__(self,other):
#         rev=int(str(other.a)[::-1])
#         return f'{self.a} + {rev} = {self.a+rev}'

# class WeirdInt(MyInt):
#     def __init__(self,a):
#         super().__init__(a)
#     def __add__(self,other):
#         revv=int(str(self.a)[::-1])
#         return f'{other.a} + {revv} = {other.a+revv}'
    
# print(" *** Weird Integer ***")
# a,b = input("Enter a b : ").split()
# a = MyInt(a)
# b = WeirdInt(b)
# print(f"{a} + {b} => {a+b}")
# print(f"{b} + {a} => {b+a}")


# class MyInt:
#     def __init__(self,x):
#         self.x=int(x)
#     def __str__(self):
#         return f'{self.x}'
#     def __add__(self,other):
#         rev=int(str(other.x)[::-1])
#         ans=self.x+rev
#         return f'{self.x} + {rev} = {ans}'

# class WeirdInt(MyInt):
#     def __add__(self,other):
#         revv=int(str(self.x)[::-1])
#         revvv=int(str(other.x)[::-1])
#         anss=revv+revvv
#         return f'{revv} + {revvv} = {anss}'
    
# print(" *** Weird Integer II ***")
# a,b = input("Enter a b : ").split()
# a = MyInt(a)
# b = WeirdInt(b)
# print(f"{a} + {b} => {a+b}")
# print(f"{b} + {a} => {b+a}")

#  *** Weird Integer II ***
# Enter a b : 123 456
# 123 + 456 => 123 + 654 = 777
# 456 + 123 => 654 + 321 = 975
# 123 - 456 => 123 - 654 = -531
# 456 - 123 => 654 - 321 = 333
