# hi='A'
# hola='a'

# print(ord(hi))
# print(ord(hola))

# sawadee=ord(hola)-32
# print(chr(sawadee))

# for a in 'python':
#     print(a)

# for b in ['Mosh','John','Kyi']:
#     print(b)

# for c in [1,2,3,4]:
#     print(c)

# a='a'
# abc=0
# for ans in range(26):
#     abc=ans+ord(a)


#     print(chr(abc).upper())

# price=[20,30,40]
# total=0
# for prices in price:
#     total=total+prices
#     print(prices)
#     print(price)
# print(total)
# print(prices)

# for x in range(4):
#     for y in range(4):
#         print(f'({x},{y})')

# number=[4,1,4,1,4]
# for count in number:
#     print('x'*count)

# names=['lwin','moe','aung','thae','moe']
# print(names[0:3])

# x=2.56
# print(round(x))

# name = 'Lwin Moe Aung'
# print(name.replace('Lwin','Lien'))
# print(name.upper())
# print(name.lower())



# lists=[1,9,7,5,0]
# max=lists[0]
# second_largest=0
# third=0
# for com in lists:
#     if com>max:
#         max=third
#         third=second_largest
#         second_largest=com
        
# print(third,second_largest,max)

# print()

# lists=[1,9,7,5,8]
# max=lists[0]
# second_largest=0
# for com in lists:
#     if max<com:
#         com=second_largest
#         max=second_largest

# print(max,second_largest)
# print()

lists=[1,9,5,3,2]
max=lists[0]
second_largest=0
for com in lists:
    if com>max:
        max=second_largest
        second_largest=com

print(second_largest,max)

print()

lists=[1,9,7,5,0]
max=lists[0]
second_largest=0
third=0
for com in lists:
    if com>max:
        max=second_largest
        second_largest=third
        third=com
        
print(third,second_largest,max)

print()

# lists=[1,9,7,5,0]
# max=lists[0]
# second_largest=0
# third=0
# fourth=0
# for com in lists:
#     if com>max:
#         max=fourth
#         third=max
#         second_largest=third
#         max=max
        
# print(fourth,third,second_largest,max)

# a='K'
# x=ord(a)
# ans=0
# k=2

# for j in range(0,)
#     k=k-2


# for i in range(4,-1,-1):
#     ans=(x+k)+i
#     ans=x+i
#     print(chr(ans),end='')

    # k=k-2

#k is odd+1
#range is odd