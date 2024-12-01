print(' *** Alphabet Sequence (A-Z) ***')           #Print the Header
user=input('Enter character step length : ')        #Get the input
alpha,step,length=user.split()                      #Split the input into each one
ans=0                                               #To make calculation
step=int(step)                                      #change it to integer
length=int(length)                                  #change it to integer
x=ord(alpha)                                        #Make the ascii value
if x<91:                                            #Checking the input number not greater than 91
    for i in range(0,length*step,step):             #Loop to make calculation
        ans=x+i                                     #Calculation
        while ans>90:                               #Add a loop
            x=x-26                                  #Every time the value exceed than 90, just subtract 
            ans=ans-26                              #Every time the value exceed than 90, just subtract 
        print(chr(ans),end='')                      #Print the result
        if i<(length*step)-step:                    #Condition for printing '='
            print('=',end='')                       #Printing '='
    print()                                         #Line spacing
else:                                               #If the input number is something else
    print('Invalid input !!!')                      #Just print this line
print('===== End of program =====')                 #End