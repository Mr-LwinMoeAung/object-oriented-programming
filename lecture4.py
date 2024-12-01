# z=[1,2]
# y=[3,4]

# x=z+y
# print(x)

# z=[1,2,3,4,5,6,7]
# print(z[:])
# print(z[:3])
# print(z[3:4])
# print(z[3:5])
# print(z[::-1])
# a=z
# b=z
# print(a,b)
# a[2]=777
# print(a)
# print(b)

# x=[1,2,3,4]
# a=[]
# for i in x:
#     a.append(i)
# print(a)

# x=[1,2,3,4]
# a=list(x)
# print(a)

# x=[1,2,3,3.5,'Lien']
# print(x)

# x=[[1,2,3],1,2,3,4,'Lien']
# print(x)

# x=[1,2]
# a,b=x
# print(a,b)

# x=[1,2,3,4,5]


# i,*j=[1,2,3,4,5]
# print(i,j)

# *a,b=[1,2,3,4,5]
# print(a,b)

# a,*b,c=[1,2,3,4,5]
# print(a,b,c)

# input="3 4 5"
# a,b,c=input.split()
# print(a,b,c)

# x=[10,12,93,42]
# sum=0
# for i in x:
#     sum+=i
# print(f'sum={sum}')

# print('Oddddd number')
# x=[10,12,93,42,11]
# sum=0
# for i in x:
#     if i%2!=0:
#         sum+=i
# print(f'sum={sum}')

# x=[1,2,3,4,5,6,7]
# y=[]
# x.append(7)
# print(x)
# y.append(x[0])
# print(y)


# x.pop()
# print(x)

# print(x.count(7))


# x[2]=7
# print(x)

# x.count(7)
# print(x)

# x.insert(3,9)
# print(x)

# x.remove(7)
# print(x)

# x.clear()
# print(x)

# name='Lwin Moe Aung'
# name[:5]
# name[5:]
# name[6:9]
# name[::-1]
# name[0]

# m='message'
# name+m
# name*3

# 'a'=='a'
# 'a'==chr(97)
# 'a'==chr(0x41)
# 'a'==chr(0x61)
# 'a'<'b'
# 'abc'<'b'

# name.upper()
# name.lower()

# x='a b c'

# x.lstrip()
# x.rstrip()
# x.strip()

# len(x)


# def function_name():
#     return "abc"
# x=function_name()
# print(x)

# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# x=maximum(10,20)
# print(x)

# def maximum(a=10,b=20):
#     if a>b:
#         return a
#     else:
#         return b
# x=maximum(33)
# print(x)


# def isPrime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# print(' *** Prime numbers ***')
# str=input('Enter an integer : ')
# num=int(str)

# for i in range(2,num):
#     if isPrime(i):
#         print(i)

# print(' Summation of vowels index')
# str=input('Enter something : ')
# sum=0
# for i,x in enumerate(str):
#     if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
#         sum+=i
#     print(f"i={i} x={x}")
# print(f'Summation = {sum}')