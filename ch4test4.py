class MyInt:                                #Create a class
    def __init__(self, n):                  #Constructer for 1variable
        self.num = n
        
    def isPrime(self):
        if self.num < 2:                    #Checking prime numbers
            return False
        for i in range(2,self.num):         #Prime number start from 2
            if self.num % i == 0:
                return False                
        return True

    def showPrime(self):                    #To shoow prime numbers
        primes = []                         #Make an array first
        for i in range(2, self.num + 1):    
            if MyInt(i).isPrime():          #Checking primes
                primes.append(str(i))       #If there are prime , append to primes
        if len(primes)==0:                  #If there is no prime numbers
            return '!!!A prime number is a natural number greater than 1'   #Print like this
        else:
            return " ".join(primes)         #Reason- not to the numbers in the array box

    def __add__(self, b):
        return self.num + b.num             #Adding 

    def __sub__(self, b):
        return int(self.num) - int(b.num / 2)   #Calculation accroding to the task

print(" *** class MyInt ***")
a, b = input("Enter 2 number : ").split()
num1 = MyInt(int(a))
num2 = MyInt(int(b))
print(a, "isPrime =>", num1.isPrime())
print(b, "isPrime =>", num2.isPrime())
print("Prime number between 2 and", a, "=>", num1.showPrime())
print("Prime number between 2 and", b, "=>", num2.showPrime())
print(a, "-", b, "=>", num1 - num2)