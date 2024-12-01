# class Sphere:
#     def __init__(self,radius):
#         self.radius=radius
#     def changeR(self,radius):
#         self.radius=radius
#     def findVolume(self):
#         return (4/3)*pi*(self.radius)**3
#     def findArea(self):
#         return 4*pi*(self.radius)**2
#     def __str__(self):
#         return f'Radius={self.radius} \nVolume= {self.findVolume():0.6f} \nArea= {self.findArea():0.2f}\n'
#     def getattribute(self):
#         l=[]
#         for i in dir(self):
#             if i[0:2]!='__':
#                 l.append(i)
#         return l

# pi = 3.14159265853
# r1, r2 = input("Enter r1 r2 : ").split()
# sphere1 = Sphere(int(r1))
# print(type(sphere1))
# print(sphere1.getattribute())
# print(sphere1)
# sphere1.changeR(int(r2))
# print(sphere1)




# class Point:
#     def __init__(self,inte1,inte2=None):
#         if inte2 is not None:
#             self.a=int(inte1)
#             self.b=int(inte2)
#         else:
#             a,b=inte1.split()
#             self.a=int(a)
#             self.b=int(b)

#     def __str__(self):
#         return f'({self.a},{self.b})'
#     def __add__(self,other):
#         pass
#     def midPoint(self,other):
#         return f'{(self.a+other.a)/2,(self.b+other.b)/2}'
#     def distance(self,other):
#         return f'{((other.a-self.a)**2+(other.b-self.b)**2)**0.5}'


# print(" *** Class Point ***")
# in1, in2 = input("Enter x1 y1 / x2 y2 : ").split('/')
# print(f"in1= '{in1}' in2= '{in2}'")
# p1 = Point(in1)
# print("p1 =", p1)
# p2x, p2y = in2.split()
# p2 = Point(p2x, p2y)
# print("p2 =", p2)
# print(f"Middle point = {p1.midPoint(p2)}")
# print(f"distance = {p1.distance(p2)}")


# class Calculator:
#     def __init__(self,value):
#         self.value=value
#     def __str__(self):
#         return f'{self.value}'
#     def __add__(self,other):
#         return self.value+other.value
#     def __sub__(self,other):
#         return self.value-other.value
#     def __mul__(self,other):
#         return self.value*other.value
#     def __truediv__(self,other):
#         ans=self.value/other.value
#         if ans%1==0:
#             return int(ans)
#         else:
#             return F'{ans:0.3f}'
    
# print(" *** Weired calculator ***")
# x, y = input("Enter num1 num2 : ").split(",")
# x, y = Calculator(int(x)), Calculator(int(y))
# print(f"x = {x}  y = {y}")
# print(f"x+y = {x+y}")
# print(f"x-y = {x-y}")
# print(f"x*y = {x*y}")
# print(f"x/y = {x/y}")


# class MyInt:
#     def __init__(self,n):
#         self.num=int(n)
#     def isPrime(self):
#         if self.num<2:
#             return 'False'
#         for i in range(2,self.num):
#             if self.num%i==0:
#                 return False
#         return True
#     def showPrime(self):
#         new=[]
#         s=''
#         for i in range(2,self.num+1):
#             if MyInt(i).isPrime():
#                     new.append(i)
#         for i in new:
#             s+=str(i)+' '
#         return s
#     def __add__(self,b):
#         pass
#     def __sub__(self,b):
#         return self.num-b.num//2

# print(" *** class MyInt ***")
# a, b = input("Enter 2 number : ").split()
# num1 = MyInt(int(a))
# num2 = MyInt(int(b))
# print(a, "isPrime =>", num1.isPrime())
# print(b, "isPrime =>", num2.isPrime())
# print("Prime number between 2 and", a, "=>", num1.showPrime())
# print("Prime number between 2 and", b, "=>", num2.showPrime())
# print(a, "-", b, "=>", num1 - num2)


# class Rational:
#     def __init__(self,a=1,b=1):
#         self.a=a
#         self.b=b

#     def __str__(self):
#         if self.a==1 and self.b==1: 
#             return f'{self.a}'
#         else:
#             return f'{self.a}/{self.b}'
    
#     def __lt__(self,other):
#         if (self.a/self.b) < (other.a/other.b):
#             return 'TRUE'
#         else:
#             return 'FALSE'
#     def __gt__(self, other):
#         if self.a/self.b > other.a/other.b:     #Checking A is greater than B
#             return "TRUE"                           #Just printing capital letter
#         else:
#             return "FALSE"

#     def __le__(self, other):
#         if self.a/self.b <= other.a/other.b:    #Checking A is less than or equal B
#             return "TRUE"                           #Just printing capital letter
#         else:
#             return "FALSE"

#     def __ge__(self, other):
#         if self.a/self.b >= other.a/other.b:    #Checking A is greater than or equal B
#             return "TRUE"                           #Just printing capital letter
#         else:
#             return "FALSE"

#     def __eq__(self, other): 
#         if self.a/self.b == other.a/other.b:    #Checking equal A and B
#             return "TRUE"                           #Just printing capital letter
#         else:
#             return "FALSE"

#     def __ne__(self, other):
#         if self.a/self.b != other.a/other.b:    #Checking Not equal A and B
#             return "TRUE"                           #Just printing capital letter
#         else:
#             return "FALSE"
#     def __add__(self,other):
#         q=(self.a*other.b)
#         w=(self.b*other.a)
#         up=q+w
#         down=(self.b*other.b)
#         for i in range(2,10):
#             if up%i==0 and down%i==0:
#                 up=up/i
#                 down=down/i
#         return f'{int(up)}/{int(down)}'
        
#     def __sub__(self,other):
#         return (self.a/self.b)-(other.a/other.b)

    
# print(" *** Rational Calculator ***")
# print(" *        A = n1/d1        *")
# print(" *        B = n2/d2        *")
# print(" ***************************\n")
# str_input = input("Enter n1 d1 n2 d2 : ")
# n1, d1, n2, d2 = [int(e) for e in str_input.split()]
# A = Rational(n1,d1)     # A = n1/d1
# B = Rational(n2,d2)     # B = n2/d2
# C = Rational()          # C = 1/1      
# print("A = ",A,"\tB = ",B,"\tC = ",C) #method __str__
# print("A < B ==> ",A<B)     # method __lt__
# print("A > B ==> ",A>B)     # method __gt__
# print("A <= B ==> ",A<=B)   # method __ge__
# print("A >= B ==> ",A>=B)   # method __gt__
# print("A == B ==> ",A==B)   # method __eq__
# print("A != B ==> ",A!=B)   # method __ne__
# print("A + B ==> ",A+B)     # method __add__

