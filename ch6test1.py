class A:                                            #Create a class
    def __init__(self,name,age):                    #Initialize objects of that class
        self.name=name
        self.age=age

class B(A):                                         #B inherits the class A and now, we can have the property of class A
    def __init__(self, name, age):                  #Initialize objects of that class
        A.__init__(self,name,age)
    def __str__(self):                              #For printing
        return f'name={self.name} age={self.age}'   #Print formally

print(" *** B inherit A ***")
name,age = input("Enter name age : ").split()
b = B(name,age)
print(b)