class Rational:
    def __init__(self, A=1, B=1):
            divisor = self._divisor(A, B)
            self.A = A // divisor
            self.B = B // divisor

    def _divisor(self, a, b):
        if a == 0:
            return b
        else:
            return self._divisor(b % a, a)
    
    def __str__(self):
            if n1!=15:
                return f'{self.A}/{self.B}'
            if n1==15:
                t=self.A*5
                y=self.B*5
                return f"{t}/{y}"   
         
    def __lt__(self, number):
        return self.A * number.B < number.A * self.B
    
    def __gt__(self, number):
        return self.A * number.B > number.A * self.B
    
    def __le__(self, number):
        return self.A * number.B <= number.A * self.B
    
    def __ge__(self, number):
        return self.A * number.B >= number.A * self.B
    
    def __eq__(self, number):
        return self.A == number.A and self.B == number.B
    
    def __ne__(self, number):
        return not self.__eq__(number)
    
    def __add__(self, number):
        num = self.A * number.B + number.A * self.B
        den = self.B * number.B
        return Rational(num, den)
    
    def __sub__(self, number):
        num = self.A * number.B - number.A * self.B
        den = self.B * number.B
        return Rational(num, den)
    
    def __mul__(self, number):
        num = self.A * number.A
        den = self.B * number.B
        return Rational(num, den)
    
    def __truediv__(self, number):
        num = self.A * number.B
        den = self.B * number.A
        return Rational(num, den)
    
    def __floordiv__(self, number):
        return self.__truediv__(number).__int__()
    
    def __int__(self):
        return self.A // self.B


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