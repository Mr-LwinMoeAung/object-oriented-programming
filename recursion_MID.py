#Function call itself
#Two cases - Base case / first think it
#Recursive case: calling itself

# def factorial(n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))


# def walk(step):
#     if step==0:
#         return
#     walk(step-1)
#     print(f'walking {step}')

# print(walk(5))


# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
    
# print(fibo(7))

# def stair(n,a=1):
#     if n==0:
#         return
#     elif n>=a:
#         print('_'*(n-a) + '#' * a)
#         stair(n,a+1)
# stair(5)

# def rev(n):
#     if len(n)==1:
#         return n
#     else:
#         return rev(n[1:])+n[0]

# print(rev('LWIN'))


# def test(n,i=0):

#     if i==len(n):
#         return
#     elif i<len(n):
#         if i%2==0:
#             print(n[i]+'*',end='')
#             test(n,i+1)
#         else:
#             print(n[i]+'~',end='')
#             test(n,i+1)

# def leng(x,j=0):
#     if x[j]==x[-1]:
#         return j+1
#     else:
#         return leng(x,j+1)

# inp='lwin'
# length=leng(inp)
# print(length)
# test(inp)