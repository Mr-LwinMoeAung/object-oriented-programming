class MyInt:                                #Create a class
    def __init__(self,a):                   #Initialize objects of that class
        self.a=int(a)
    def __add__(self,other):                #__add__ method to sun the values
        rev = int(str(other.a)[::-1])       #Reverse the order
        result = self.a + rev               #Sum the 'a' value and reversed 'b'
        return f"{self.a:,} + {other.a:,} = {self.a:,} + {rev:,} = {result:,}"  #Print according to the task
    def __str__(self):                      #Printing method
        return str(self.a)                  #To print the original value of 'a' and 'b' for this "{a} + {b}"

class WeirdInt(MyInt):                      #Class:WeirdInt inherits the MyInt class
    def __init__(self,a):                   #Initialize objects of that class
        super().__init__(a)                 #Use super() to  call __init__ method in a parent class from a subclass
    def __add__(self,other):                #Just like above __add__ method, just change other and self
        revv=int(str(self.a)[::-1])
        result=revv+other.a
        return f'{self.a:,} + {other.a:,} = {revv:,} + {other.a:,} = {result:,}'    #Printing formally

print(" *** Weird Integer ***")
a,b = input("Enter a b : ").split()
a = MyInt(a)
b = WeirdInt(b)
print(f"{a} + {b} => {a+b}")
print(f"{b} + {a} => {b+a}")