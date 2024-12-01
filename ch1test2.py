print(' *** BMI Calculator *** ')                               #To print the header
user_input=input('Enter your Height(m) and Weight(kg) : ')      #Declare a variable named 'user_input', Get the input from user as a 'string type'
height,weight=user_input.split()                                #Split the input string value from 'user_input' to height and weight
w=float(weight)                                                 #Convert the string type into float as 'w'
h=float(height)                                                 #Convert the string type into float as 'h'
BMI=w/(h**2)                                                    #Make the calculation and named 'BMI'
if BMI<18.5:                                                    #Create a condition - if 'BMI value is greater than 18.5
    print('Less Weight')                                        #if the above condition is true = print 'Less Weight' 
elif 18.5<=BMI and BMI<23:                                      #else if the 'BMI' is equal and between 18.5 and 23 but not greater than 23
    print('Normal Weight')                                      #if the above condition is true = print 'Normal Weight'
elif 23<=BMI and BMI<25:                                        #else if 'BMI' is equal and between 23 and 25 but not greater than 25
    print('More than Normal Weight')                            #if the above condition is true = print 'More than Normal Weight'
elif 25 <= BMI and BMI < 30:                                    #else if 'BMI' is equal and between 25 and 30 but not greater than 30
    print('Getting Fat')                                        #if the above condition is true = print 'Getting Fat'
else:                                                           #if the above all conditions are not true
    print('Fat')                                                #print 'Fat'