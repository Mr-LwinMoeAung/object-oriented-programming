class Calculator:                           #Create a class
    def __init__(self, x=0):                #Constructor for 1 value
        self.value = x  

    def __str__(self):
        return str(self.value)              #Printing according to the given code

    def __add__(self, new):
        return self.value + new.value       #Add two numbers

    def __sub__(self, new):                 
        return self.value - new.value       #Sub two numbers

    def __mul__(self, new):
        return f'{self.value}{new.value}'   #Combine two numbers

    def __truediv__(self, new):
        ans=self.value / new.value          #Divide two numbers
        check=ans%1                         #To print according to the task
        if check==0:                         
            ans=int(ans)                    #If there is no decimal , change it to integer
            return ans
        else:
            return f'{ans:0.3f}'            #To print decimal 3 points

print(" *** Weired calculator ***")
x, y = input("Enter num1 num2 : ").split(",")
x, y = Calculator(int(x)), Calculator(int(y))
print(f"x = {x}  y = {y}")
print(f"x+y = {x+y}")
print(f"x-y = {x-y}")
print(f"x*y = {x*y}")
print(f"x/y = {x/y}")