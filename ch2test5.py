print(' *** Pyramid-XV ***')                        #Print the Header
user=int(input('Enter height : '))                  #Get the input from user and change it to integer
adding=0                                            #To use in calculation
a=ord('A')                                          #Use the first capital alplabet and ascii number of it
reversing=[]                                        #To make reverse printing for each even line
count=0                                             #An array to use in reverse printing
new_count=3                                         #Variable to use in reverse printing
for i in range(user):                               #Loop for the row 
    for j in range((user-1)-i):                     #Make a loop to print the '-'
        print('-',end='')                           #Print '-'
    if  i%2!=0:                                     #Condition to check odd lines
        for j in range(i):                          #Loop to print '.'
            print('.',end='')                       #Print the '.' in odd lines in order
    for z in range(i+1):                            #Loop to print alphabet in colum
        if i%2!=0 or i==0:                          #Checking the odd lines
            process=a+adding                        #If odd line, make calculation
            print(chr(process),end='')              #Print the alphabets
            if process>=90:                         #Checking the ascii value ,equal or greater than 90
                process=ord('A')                    #If the above condition is true, change it back to the ascii of first capital alphabet
                adding=0                            #Also the increasement back to zero
            else:                                   #Else
                adding+=1                           #Make the increasement
        if i%2==0 and i!=0:                         #Checking even lines
            count+=1                                #If the above condition is ture, start increae the count to use in reverse order
            process=a+adding                        #Calculation
            process=chr(process)                    #Set ascii value to character
            reversing.append(process)               #Put the incoming characters into an array 
            if count==new_count:                    #Condition to check equal to 3,5,7,9...etc.
                reversing=reversing[::-1]           #Reverse the order
                for char in range(len(reversing)):  #Array printing loop
                    print(reversing[char],end='')   #Printing reverse alphabets
                new_count+=2                        #Plus 2 to 'new_count' in every single loop
                reversing=[]                        #Empty the array in every single loop after finish the printing
                count=0                             #Set the 'count' back to zero 
            if ord(process)>=90:                    #Check the ascii value greater than or equal to 90
                process=ord('A')                    #If the above condition is true, change it back to the ascii of first capital alphabet
                adding=0                            #Also the increasement back to zero
            else:                                   #Else
                adding+=1                           #Make increasement
    if i%2==0 and i!=0:                             #Condition to check the even lines
        for j in range(i):                          #Loop to print '.'
            print('.',end='')                       #Printing '.'
    for j in range((user-1)-i):                     #Loop to print '-'
        print('-',end='')                           #Printing '-'
    print()                                         #Line spacing
print('===== End of program =====')                 #End