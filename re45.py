class Rational:
    def __init__(self,n1=1,d1=1):           #Constructor for 2 variables
        self.n1=n1                          
        self.d1=d1

    def __str__(self):      
        if self.d1 == 1:
            return f"{self.n1}"             #Printing formally for C is always 1
        else:
            return f'{self.n1}/{self.d1}'   #printing formally
    
    def __lt__(self, other):
        if self.n1/self.d1 < other.n1/other.d1: #Checking A is less than B? 
            return "TRUE"                       #Just printing capital letter
        else:
            return "FALSE"                      

    def __gt__(self, other):
        if self.n1/self.d1 > other.n1/other.d1:     #Checking A is greater than B
            return "TRUE"                           #Just printing capital letter
        else:
            return "FALSE"

    def __le__(self, other):
        if self.n1/self.d1 <= other.n1/other.d1:    #Checking A is less than or equal B
            return "TRUE"                           #Just printing capital letter
        else:
            return "FALSE"

    def __ge__(self, other):
        if self.n1/self.d1 >= other.n1/other.d1:    #Checking A is greater than or equal B
            return "TRUE"                           #Just printing capital letter
        else:
            return "FALSE"

    def __eq__(self, other): 
        if self.n1/self.d1 == other.n1/other.d1:    #Checking equal A and B
            return "TRUE"                           #Just printing capital letter
        else:
            return "FALSE"

    def __ne__(self, other):
        if self.n1/self.d1 != other.n1/other.d1:    #Checking Not equal A and B
            return "TRUE"                           #Just printing capital letter
        else:
            return "FALSE"
        
    def __add__(self,other):                        #Adding A and B
        x=(self.n1*other.d1)+(other.n1*self.d1)     #Calculation for adding two rational numbers
        y=(self.d1*other.d1)                      
        for i in range(2,10):                       #Checking the rational number can be divided by 2-10, to get the final rational number
            if x%i==0 and y%i==0:                   #Checking the divisible numbers
                x=int(x/i)
                y=int(y/i)
                if x%i==0 and y%i==0:        #Checking again, For example: 4 can be divisible by 2 for two times, then we will get 1, just like that
                    x=int(x/i)
                    y=int(y/i)
        if x/y==1:                                  #if x is divided by y equal to 1, the ouput will be 1
            return f'1' 
        elif y==1:                                  #If y is 1, we don't need to print it
            return f'{x}'
        else:                                       #Else, we just need to print according to the task
            return f'{x}/{y}' 
    
    def __sub__(self,other):                        #Subtraction explaination => Just like the adding two numbers
        x=(self.n1*other.d1)-(other.n1*self.d1)     #We just need to change minus operator
        y=(self.d1*other.d1)
        for i in range(2,10):                       #Just like the explanation of __add__ function
            if x%i==0 and y%i==0:
                x=int(x/i)
                y=int(y/i)
                if x%i==0 and y%i==0:
                    x=int(x/i)
                    y=int(y/i)
        if x/y==1:
            return f'1' 
        elif y==1:
            return f'{x}'
        else:
            return f'{x}/{y}' 
    
    def __mul__(self,other):                        #Multiplication
        x=(self.n1*other.n1)                        #Calculation for x
        y=(self.d1*other.d1)                        #Calculation for y
        for i in range(2,10):                       #Just like the explanation of __add__ function
            if x%i==0 and y%i==0:
                x=int(x/i)
                y=int(y/i)
                if x%i==0 and y%i==0:
                    x=int(x/i)
                    y=int(y/i)
        if x/y==1:
            return f'1' 
        elif y==1:
            return f'{x}'
        else:
            return f'{x}/{y}' 
    
    def __truediv__(self,other):                    #Division
        x=(self.n1*other.d1)                        #Calculation for x
        y=(self.d1*other.n1)                        #Calculation for y
        for i in range(2,10):                       #Just like the explanation of __add__ function
            if x%i==0 and y%i==0:
                x=int(x/i)
                y=int(y/i)
                if x%i==0 and y%i==0:
                    x=int(x/i)
                    y=int(y/i)
        if x/y==1:
            return f'1' 
        elif y==1:
            return f'{x}'
        else:
            return f'{x}/{y}' 
    
    def __floordiv__(self,other):                   #Like __truediv__ function, now we need to divide x by y to get only one integer
        x=(self.n1*other.d1)                        
        y=(self.d1*other.n1)
        for i in range(2,10):                       #Just like the explanation of __add__ function
            if x%i==0 and y%i==0:
                x=int(x/i)
                y=int(y/i)
                if x%i==0 and y%i==0:
                    x=int(x/i)
                    y=int(y/i)
        ans=x//y                                    #To get only one output integer according to the task
        return ans

    
print(" *** Rational Calculator ***")
print(" *        A = n1/d1        *")
print(" *        B = n2/d2        *")
print(" ***************************\n")
                        
str_input = input("Enter n1 d1 n2 d2 : ")
n1, d1, n2, d2 = [int(e) for e in str_input.split()]
A = Rational(n1,d1)     # A = n1/d1
B = Rational(n2,d2)     # B = n2/d2
C = Rational()          # C = 1/1      
print("A = ",A,"\tB = ",B,"\tC = ",C) # method __str__
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