# user=int(input('Enter : '))
# ans=0
# j=0
# print('Summation => ',end='')
# for i in range(1,user+1):
#     j+=1
#     ans+=i
#     print(i,end='')
#     if j<user:
#         print('+',end='')
# print(f' = {ans}')




# user=input('Enter : ')
# intt=int(user)
# print (f'Number = {intt:,}')
# print('Total digits are = ',end='')
# new=[]
# ans=0

# for i in user:
#     new.append(int(i))

# for i in new:
#     ans+=i
# print('Summation = ',end='')
# print(ans)




# user=input('Enter : ')
# alpha,step,leg=user.split()

# step=int(step)
# leg=int(leg)

# a=ord(alpha)
# ans=0
# print(a,step,leg,alpha)
# print(ord('Z'))
# for i in range(0,leg*step,step):
#     ans=a+i
#     if ans>90:
#         a=a-26
#         ans=ans-26
#     print(chr(ans),end='')


# user=int(input('Enter : '))
# a=ord('A')
# for i in range(user):
#     for j in range(user-i-1):
#         print(' ',end='')
#     for k in range(i+1):
#         print('#',end='')
#     for z in range(i):
#         print('#',end='')
#     print()