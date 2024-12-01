user=int(input('Enter number : '))

for i in range(user):
    for j in range(i):
        print(' ',end='')
    for k in range(user-i):
        print('*',end='')
    for x in range(user-i-1):
        print('*',end='')
    for y in range(1):
        print(' / ', end='')
    for z in range(i+1):
        print('*',end='')
    for a in range(i):
        print('*',end='')
    print()