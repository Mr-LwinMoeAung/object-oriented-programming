print(' *** integer summation from 1 to n *** ')  #Header
user = int(input('Enter an integer(n) : '))       #Get input and change it to integer
total=0                                           #Declare a variable to make the summation
j=0                                               #To add to the summation
print('Summation => ',end='')                     #Printing
for i in range(user):                             #Loop and make calculation inside it
    j+=1                                          #Plus 1 to 'j' each looping
    total+=j                                      #Calculation for total summation
    print(f'{j}',end='')                          #To print the numbers
    if i<user-1:                                  #Condition for printing '+' sign
        print('+',end='')                         #Printing
print(f' = {total}')                              #Printing the final summation result