print(' *** Triangle Checking ***')             #print the header
user=input('Enter 3 sides : ')                  #Declare a variable and Get the input from the user
x,y,z=user.split()                              #Slpit the three input values to x and y and then z 
x=int(x)                                        #Change the string type to integer type
y=int(y)                                        #Change the string type to integer type
z=int(z)                                        #Change the string type to integer type
                                                #In this part, I can write with "try:except:" but I think using "if:else:" is more natural
if(x>0 and y>0 and z>0):                        #I want all the inputs must grater than 0 and this is the main condition
    if x>=y and x>=z:                           #Checking 'x' is the greatest or not
        if y>z:                                 #if 'x' is the greatest, Check 'y or z' is second greatest
            print(f'max={x} mid={y} min={z}')   #According to the above condition, print it
        elif z>y:                               #if 'x' is the greatest, Check 'y or z' is second greatest
            print(f'max={x} mid={z} min={y}')   #According to the above condition, print it
        else:                                   #If there is no second greatest in "y and z", they should be equal and both can be 'mid'
            print(f'max={x} mid={y} min={z}')   #According to the above condition, print it
    if y>x and y>z:                             #Checking 'y' is the greatest or not
        if x>z:                                 #if 'y' is the greatest, Check 'x or z' is second greatest
            print(f'max={y} mid={x} min={z}')   #According to the above condition, print it
        elif z>x:                               #if 'y' is the greatest, Check 'z or x' is second greatest
            print(f'max={y} mid={z} min={x}')   #According to the above condition, print it
        else:                                   #If there is no second greatest in "z and x", they should be equal and both can be 'mid'
            print(f'max={y} mid={x} min={z}')   #According to the above condition, print it
    if z>x and z>y:                             #Checking 'z' is the greatest or not
        if x>y:                                 #if 'z' is the greatest, Check 'x or y' is second greatest
            print(f'max={z} mid={x} min={y}')   #According to the above condition, print it
        elif y>x:                               #if 'z' is the greatest, Check 'x or y' is second greatest
            print(f'max={z} mid={y} min={x}')   #According to the above condition, print it
        else:                                   #If there is no second greatest in "y and x", they should be equal and both can be 'mid'
            print(f'max={z} mid={x} min={y}')   #According to the above condition, print it
    if (x>1 or y>1 or y>1) and (x==y!=z or x==z!=y or y==x!=z or y==z!=x or z==x!=y or z==y!=x): #Make the condition for ISOSCELES triangle
        print(f'{x}, {y} and {z} are sides of ISOSCELES triangle.')                              #According to the above condition, print it
    elif x==y==z:                                                                                #Make the condition for ISOSCELES triangle
        print(f'{x}, {y} and {z} are sides of EQUIlATERAL triangle.')                            #According to the above condition, print it
    elif x!=y!=z!=x and (x-1!=y or y-1!=z):                                                      #Make the condition for ISOSCELES triangle
        print(f'{x}, {y} and {z} are sides of RIGHT triangle.')                                  #According to the above condition, print it
    elif x-1==y and y-1==z:                                                                      #Make the condition for ISOSCELES triangle
        print(f'{x}, {y} and {z} are sides of SCALENE triangle.')                                #According to the above condition, print it
    else:                                                                                        #If there is no match with above conditions
        print(f'{x}, {y} and {z} are not side of triangle.')                                     #According to the above condition, print it
else:                            #It is the else for the main condition, if the input is equal to 0, the program will jump to this condition
    print('Invalid input !!!')   #According to the above condition, print it
    quit()                       #Make the program to end