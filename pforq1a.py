# x=12345

# a=x%10
# b=x//10%10
# c=x//100%10
# d=x//1000%10

# #base 16
# print(f'{x:X}')
# #right 8binary
# print(f'{x//16%16:04b} {x%16:04b}')
# print(a,b,c,d)

# fl=1.2345
# print(f'{fl%1:0.5f}')
# print(f'{fl//1}')
# q=int((fl*10)%10)
# w=int((fl*100)%10)
# print(q,w)

# e=17

# print('Summation => ',end='')
# total=0
# j=0
# for i in range(e):
#     j+=1
#     total+=j
#     print(j,end='')
#     if i<e-1:
#         print('+',end='')
# print(f' = {total}')


# user1=6
# a=65
# ans=0
# for i in range(user1):
#     b=a+ans
#     for j in range(user1-i-1):
#         print(' ',end='')
#     for j in range(i+1):
#         print(chr(b),end='')
#         ans+=1
#         b+=1
#     for j in range(i):
#         print(chr(b),end='')
#         ans+=1
#         b+=1
#     print('')

# user2='12345678111'
# list1=[]
# ans=0
# for i in user2:
#     list1.append(int(i))
# print(list1)

# for i in range(len(list1)):
#     ans+=list1[i]
# print(ans)


# print(' *** Remove Duplicate ***')          #Printing Header
# user = input('Enter numbers : ')            #Getting input
# list1=user.split()
# print(list1)
# new=[]
# sum=0
# for i in list1:
#     i=int(i)
#     if i not in new:
#         new.append(i)
#     else:
#         sum+=i
# print(new)
# print(sum)
def is_prime(num):
    """
    Check if a given number is prime or not.
    """
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_prime_numbers(arr):
    """
    Given an array of integers, return a list of the prime numbers.
    """
    prime_numbers = []
    for num in arr:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Example usage:
my_array = [3, 4, 7, 10, 13, 20, 23]
prime_numbers = get_prime_numbers(my_array)
print(prime_numbers)



def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def show(x):
    list1=[]
    k=''
    for i in x:
        if prime(i):
            list1.append(i)
    for j in range(len(list1)):
        k+=str(list1[j])+' '
    return k


arr=[1,2,3,4,5,6,7,8]

ans=show(arr)
print(ans)
