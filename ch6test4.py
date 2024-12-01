class MyInt:                                    #Create a class
    def __init__(self,a):                       #Initialize objects of that class
        self.a=int(a)

    def __add__(self,other):                    #__add__ method to sun the values
        rev=int(str(other.a)[::-1])             #Reverse the order
        result=self.a+rev                       #Sum the 'a' value and reversed 'b'
        return f'{self.a} + {rev} = {result:,}' #Print according to the task
    
    def __sub__(self,other):                    #Just like __add__ method, it is just subtract
        rev=int(str(other.a)[::-1])             
        result=self.a-rev
        return f'{self.a} - {rev} = {result:,}'
    
    def __str__(self):                          #Printing method
        return str(self.a)                      #To print the original value of 'a' and 'b' for this "{a} + {b}"
    
class WeirdInt(MyInt):                          #Class:WeirdInt inherits the MyInt class
    def __init__(self,a):                       #Initialize objects of that class
        super().__init__(a)                     #Use super() to  call __init__ method in a parent class from a subclass

    def __add__(self,other):                #Like the above __add__ method, just change other and self and reverse again
        revv=int(str(self.a)[::-1])
        revvv=int(str(other.a)[::-1])
        result=revv+revvv
        return f'{revv} + {revvv} = {result:,}'
    
    def __sub__(self,other):                #Like the above __sub__ method, just change other and self and reverse again
        revv=int(str(self.a)[::-1])
        revvv=int(str(other.a)[::-1])
        result=revv-revvv

        return f'{revv} - {revvv} = {result:,}'
    
    def __str__(self):              #Printing method
        return str(self.a)          #To print the original value of 'a' and 'b' for this "{a} + {b}"

print(" *** Weird Integer II ***")
a,b = input("Enter a b : ").split()
a = MyInt(a)
b = WeirdInt(b)
print(f"{a} + {b} => {a+b}")
print(f"{b} + {a} => {b+a}")
print(f"{a} - {b} => {a-b}")
print(f"{b} - {a} => {b-a}")