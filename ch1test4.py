print(' *** Data type integer float string *** ')    #Print the header
user_input=input('Enter a word : ')                  #Declare a variable and get the input from user
try:                                                 #try first
    value=int(user_input)                            #try to change the string type into int type and if fail, the program will go to 'except:'
    print(' === Integer Mode === ')                  #And then print it to tell the user you are in the integer mode
    print(f'{value:,} * 2 = {value*2:,}')            #Make the calculation 
    print(f'{value:,} tenth digit =',value//10%10)   #Calculation for finding 10th digit
    print(f'{value:,} base 16 = {value:X}')          #Calculation for finding base 16 and print in capital letter
    print(f'{value:,} right 8-digit binary = {value//16%16:04b} {value%16:04b}') ##print it like the description
except:                                              #if try: is failed and an error is occurred, do the except: 
    try:                                             #try it first
        value=float(user_input)                      #try to change the string type into float type and if fail, the program will go to 'except:'
        print(' === Float Mode === ')                #And then print it to tell the user you are in the float mode
        integer=value//1                             #Calculation to split the float into integer
        decimal=value%1                              #Calculation to split the float into only decimal
        print(f'{value:0.5f} = {int(integer):,} + {decimal:0.5f}')  #print it like the description
        first_decimal=(value*10)%10                  #Calculation to get the first decimal
        second_decimal=(value*100)%10                #Calculation to get the second decimal
        first_decimal=int(first_decimal)             #Change that into integer value
        second_decimal=int(second_decimal)           #Change that into integer value
        print(f'Sum of 2 decimal point digits = {first_decimal} + {second_decimal} =',first_decimal+second_decimal) #print it like the description
        print(f'{value:0.6f} = {value:0.20f}')       #print it like the description
    except:                                          #if try: is failed and an error is occurred, do the except: 
        print(' === String Mode === ')               #print it to tell the user you are in the string mode
        print(user_input,user_input*2,user_input*3)  #print it like the description