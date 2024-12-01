print(' *** Digit count and Summation ***')     #Printing the Header
user=int(input('Enter an integer : '))          #Get the input from user and change it to integer
x=str(user)                                     #Change it to string 
print((f'number = {user:,}'))                   #Printing the input number adding ',' comma
print(f'Total digits are:  {len(x)}')           #Printing the length of input number
y=int(len(x))                                   #Change the length to integer
ans=1                                           #Create the variable to make calculation
summation=0                                     #Create the variable to make calculation
a=0                                             #Create the variable to make calculation
for i in range(y-1):                            #Loop for making calculation
    ans*=10                                     #Get the 10 power to make division to get individual digit
for j in range(y):                              #Make the loop to calculate
    a=round(a)            #Make sure the calculation for the bigger input number, when the loop reach 15th time, it will be went wrong with decimal
    a=user//round(ans)    #So, I use the round() function to get the nearest number 
    a=round(a)                                  #Calculation
    a=user//round(ans)%10                       #Calculation
    summation+=a                                #Calculation
    ans=round(ans)/10                           #Calculation
print(f'Summation = {int(summation)}')          #Printing the result