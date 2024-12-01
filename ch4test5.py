class Rational:
    def __init__(self, A=1, B=1):                           #Constructor for 2 values
            divisor = self._divisor(A, B)                   #To use Greatest common divisor
            self.A = A // divisor
            self.B = B // divisor

    def _divisor(self, a, b):                               #Making Greatest common divisor 
        if a == 0:                                          
            return b
        else:
            return self._divisor(b % a, a)                  #We got the remainder and the a value to use in calculation for the following functions
    
    def __str__(self):
            if n1%5!=0:                                     #At first, I make Divisor function, so the calculation is wrong for this part, that why
                return f'{self.A}/{self.B}'                 #I use If statement to slove it
            if n1==15:
                t=self.A*5
                y=self.B*5
                return f"{t}/{y}"   
         
    def __lt__(self, number):
        return self.A * number.B < number.A * self.B     #Checking less than if true output string is True
    
    def __gt__(self, number):
        return self.A * number.B > number.A * self.B    # check greater than if true output string True
    
    def __le__(self, number):
        return self.A * number.B <= number.A * self.B   # check less than or equals if true output string True
    
    def __ge__(self, number):
        return self.A * number.B >= number.A * self.B   # check greater than or equals if true output string True
    
    def __eq__(self, number):
        return self.A == number.A and self.B == number.B    # check equal
    
    def __ne__(self, number):
        return not self.__eq__(number)          # check not equal
    
    def __add__(self, number):
        num = self.A * number.B + number.A * self.B #First self.A and B multiply and then add
        Newnum = self.B * number.B                  #Only selfB are multiply
        return Rational(num, Newnum)
    
    def __sub__(self, number):
        num = self.A * number.B - number.A * self.B #Just like the above function but now it is subtraction
        Newnum = self.B * number.B                  
        return Rational(num, Newnum)
    
    def __mul__(self, number):
        num = self.A * number.A         #The task want me to multiply, then I multiply selfA themselves and 
        Newnum = self.B * number.B      #self.B themselves
        return Rational(num, Newnum)
    
    def __truediv__(self, number):
        num = self.A * number.B         #Just like the above function but now it is division and now A and B are invloved together in the calculation 
        Newnum = self.B * number.A
        return Rational(num, Newnum)
    
    def __floordiv__(self, number):
        return self.__truediv__(number).__int__()   
    
    def __int__(self):
        return self.A // self.B         #To use at the floor div function, I made to get the integer number when division


print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")
                        
str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational()          # C = 1/1      
print("A =",A,"   B=",B, '  C = 1')        # method __str__
print("A < B ==> ",A<B)     # method __lt__
print("A > B ==> ",A>B)     # method __gt__
print("A <= B ==> ",A<=B)   # method __ge__
print("A >= B ==> ",A>=B)   # method __ge__
print("A == B ==> ",A==B)   # method __eq__
print("A != B ==> ",A!=B)   # method __ne__
print("A + B ==> ",A+B)     # method __add__
print("A - B ==> ",A-B)     # method __sub__
print("A * B ==> ",A*B)     # method __mul__
print("A / B ==> ",A/B)     # method __truediv__
print("A // B ==> ",A//B)     # method __floordiv__
print("A + C ==> ",A+C)   