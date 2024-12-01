print(' *** Pyramid-II ***')            #Header
user=int(input('Enter height : '))      #Get the input from User and change it to integer
ans=0                                   #Declare a variable equals with 0
a=ord('A')                              #Declare a variable equals with ascii value of A
for row in range(user):                 #Make a loop for row
    b=a+ans                             #Make calculation to increase the ascii value and let equal it with variable 'b'
    for col in range((user-1)-row):     #Create a loop to print ' ' space first
        print(' ',end='')               #Printing space
    if b>=91:                           #Checking the ascii value not greater than 91
        b=ord('A')                      #If the 'b' is greater than 91, we put it back to ascii value'65'
        ans=0                           #Also set the increasement to 0
        for col in range(row+1):        #Create a loop to print the alphabets
            print(chr(b),end='')        #Start printing the alphabets
            ans+=1                      #Make the increasement
            if b>=90:                   #Checking the ascii value not greater than 91
                b=ord('A')              #If the 'b' is greater than 91, we put it back to ascii value'65'
                ans=0                   #If the 'b' is greater than 91, we put it back to ascii value'65'
            else:                       #Else
                b+=1                    #Make the increasement
                ans+=1                  #Make the increasement
    else:                               #If the 'b' is not greater than 91
        for col in range(row+1):        #Create a loop to print the alphabets
            print(chr(b),end='')        #Printing the alphabets
            if b>=90:                   #Checking
                b=ord('A')              #Same as previous one
                ans=0                   #Same as previous one
            else:                       #Same as previous one
                b+=1                    #Same as previous one
                ans+=1                  #Same as previous one
    if b>=91:                           #Same as previous one
        b=ord('A')                      #Same as previous one
        for col in range(row):          #Same as previous one
            print(chr(b),end='')        #Same as previous one
            if b>=90:                   #Same as previous one
                b=ord('A')              #Same as previous one
            else:                       #Same as previous one
                b+=1                    #Same as previous one
                ans+=1                  #Same as previous one
    else:                               #Same as previous one
        for col in range(row):          #Same as previous one
            print(chr(b),end='')        #Same as previous one
            if b>=90:                   #Same as previous one
                b=ord('A')              #Same as previous one
                ans=0                   #Same as previous one
            else:                       #Same as previous one
                b+=1                    #Same as previous one
                ans+=1                  #Same as previous one
    print()                             #Line spacing
print('===== End of program =====')     #End