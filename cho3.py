# print('*** Isosceles number : ')
# user_input=input('Enter a positive integer : ')

# n=int(user_input)
# row,col=0,0

# while row<n:
#     col=0
#     while col<row:
#         print(' ',end='*')
#         col+=1
#     print()
#     row+=1
# print('End of program')

# n=int(input('Enter a number : '))

# for col in range(n):
#     for row in range(col+1,n):
#         print(' ',end='')
#     for i in range(col+1):
#         print('+',end='')
#     for j in range(col):
#         print('+',end='')
#     print()
# for col in range(n):
#     for row in range(col+1):
#         print(' ',end='')
#     for i in range(col+1,n):
#         print('+',end='')
#     for j in range(col+2,n):
#         print('=',end='')
#     print()
# print()

# for col in range(n):
#     for row in range(col+1,n):
#         print(' ',end='')
#     for i in range(col+1):
#         print('=',end='')
#     print()

# for col in range(n):
#     for row in range(col+1):
#         print(' ',end='')
#     for i in range(col+1,n):
#         print('=',end='')
#     print()

# Python Program to Print X Star Pattern
 
# rows = int(input("Enter X Pattern Odd Rows = "))

# print("X Star Pattern") 

# for i in range(0, rows):
#     for j in range(0, rows):
#         if(i == j or j == rows - 1 - i):
#             print('*', end = '')
#         else:
#             print(' ', end = '')
#     print()


# for col in range(6):
#     for row in range(7):
#         if (col==0 and row%3!=0) or (col==1 and row%3==0) or (col-row==2) or (col+row==8):
#             print('+',end='')
#         else:
#             print(' ',end='')
#     print()

# for col in range(7):
#     for row in range(7):
#         if (row==col) or (row==7-1-col):
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# a='a'
# ans=0
# i=0
# while i<26:
#     ans=i+ord(a)
#     print(chr(ans))
#     i=i+1