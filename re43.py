#  *** Weired calculator ***
# Enter num1 num2 : 6,3
# x = 6  y = 3
# x+y = 9
# x-y = 3
# x*y = 63      # concatenate the digit 6 and 3
# x/y = 2

class Calculator :
    def __init__(self,x=0):
        self.value=x
    def __str__(self):
        return str(self.value)

    def __add__(self,other):
        return self.value+other.value
    
    def __sub__(self,other):
        return self.value-other.value
    
    def __mul__(self,other):
        return f'{self.value}{other.value}'

    def __truediv__(self,other):
        ans=self.value/other.value
        check=ans%1
        if check==0:
            ans=int(ans)
            return ans
        else:
            return f'{ans:0.3f}'

print(" *** Weired calculator ***")
x,y = input("Enter num1 num2 : ").split(",")
x,y = Calculator(int(x)),Calculator(int(y))
print(f"x = {x}  y = {y}" )
print(f"x+y = {x+y}")
print(f"x-y = {x-y}")
print(f"x*y = {x*y}")
print(f"x/y = {x/y}")