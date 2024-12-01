# def duplicate(x):
#     new=[]
#     g=[]
#     sum=0
#     for i in range(len(x)):
#         x[i]=int(x[i])
#         if x[i] not in new:
#             new.append(x[i])
#         else:
#             g.append(x[i])

#     for i in range(len(g)):
#         sum+=g[i]


#     return f'newList = {new}\nsum of duplicate = {sum}'


# input=input('Enter numbers : ')
# arr=[]
# arr=input.split()
# print(duplicate(arr))


# user=input('Enter : ')
# x=user.split()

# for i in x:
#     all=''
#     mid=''
#     l=(len(i))
#     first=i[0]
#     last=i[l-1]
#     for j in range(1,l-1):
#         mid+=i[j]

#     print(last+mid+first,end=' ')


# x,y=input('Enter : ').split(' / ')
# a,b=x.split()
# a=int(a)
# b=int(b)
# lists=y.split()
# new=[]
# for i in range(len(lists)):
#     lists[i]=int(lists[i])
# copy=lists.copy()

# for j in lists:
#     if j!=a and j!=b:
#         new.append(j)

# print(f'old list = {lists}')
# print(new)


# def prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True

# user=input('Enter : ')
# new=''
# for i,char in enumerate(user):
#     if prime(i+1):
#         if char.islower():
#             new+=char.upper()
#         else:
#             new+=char.lower()
#     else:
#         new+=char
# print(new)