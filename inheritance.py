# class Parent:
#     def fun1(self):
#         print('Parent fun')

# class Child(Parent):
#     def fun2(self):
#         print('Child fun2')

# ob=Child()
# ob.fun2()
# ob.fun1()

# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def view(self):
#         print(self.name,self.age)

# class Child(Parent):
#     def __init__(self,name,age):
#         Parent.__init__(self,name,age)
#         self.last='Aung'
#     def view(self):
#         print(self.name,self.last,self.age)

# ob=Child('Lwin Moe',20)
# ob.view()

# class Parent:
#     def fun1(self):
#         print('Parent Fun1')

# class Parent2(Parent):
#     def fun2(self):
#         print('Parent2 Fun2')

# class Child(Parent):
#     def fun3(self):
#         print('Child fun2')

# ob=Child()
# ob1=Parent2()
# ob.fun1()
# ob1.fun1
# ob.fun3()

# class Parent:
#     def fun1(self):
#         print('Fun1')

# class Child(Parent):
#     def fun2(self):
#         super().fun1()
#         print('Fun2')

# ob=Child()
# ob.fun2()
