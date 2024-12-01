print(' *** Circumfernce and Area Calculator *** ')     #to print the header
pi=3.14159265853                                        #Declare a variable named 'pi' equals to its value
user_input=input('Enter radius : ')                     #Delcare a variable called user_input and Get the input from user as string type
radius=float(user_input)                                #Change that 'string' input float type
Circumference = 2*pi*radius                             #make the calculation for circumference
Area=pi*radius**2                                       #make the calculation for Area
print(f'Circumference = {Circumference:0.3f}')          #print out the Circumference value by taking into 3 decimal places
print(f'Area={Area:0.5f}')                              #print out the Area value by taking into 5 decimal places