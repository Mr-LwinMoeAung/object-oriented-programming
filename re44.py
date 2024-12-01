class MyInt:
    def __init__(self,n):
        self.num = n
        
    def isPrime(self):
        if self.num<2:
            return False
        for i in range(2,self.num):
            if self.num%i==0:
                return False
        return True

    
    def showPrime(self):
        string=' '
        lists=[]
        for i in range(2,self.num+1):
            if MyInt(i).isPrime():
                lists.append(str(i))
        if len(lists)==0:
            return '!!!A prime number is a natural number greater than 1'
        else:
            return string.join(lists)
    
    def __add__(self,b):
        pass
        
    
    def __sub__(self,b):
        return self.num-(b.num//2)

print(" *** class MyInt ***")
a,b = input("Enter 2 number : ").split()
num1 = MyInt(int(a))
num2 = MyInt(int(b))
print(a,"isPrime =>",num1.isPrime())
print(b,"isPrime =>",num2.isPrime())
print("Prime number between 2 and",a,"=>",num1.showPrime())
print("Prime number between 2 and",b,"=>",num2.showPrime())
print(a,"-",b,"=",num1-num2)