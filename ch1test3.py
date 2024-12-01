print(' *** Transform second ***')   #print the header
user_input=input('Enter seconds : ') #Get the input from user as a string type
try:                                 #try first
    time=int(user_input)             #try to change the string type into int type and if fail, the program will go to 'except:'
    week=time/604800                 #Make the calculation and change the second to week
    day_in_a_week=(time%604800)/86400 #To calculate how many days in a week
    day=time/86400                   #Make the calculation and change the second to day
    hour_in_a_day=(time%86400)/3600  #To calculate how many hours in a day
    hour=time/3600                   #Make the calculation and change the second to hour
    minute=(time%3600)/60            #Make the calculation and change the second to minute
    second=(time%60)%60              #Calculate the extra second that will be last when the calculation was ended
except:                              #if try: is failed and an error is occurred, do the except: 
    print(f'! ! ! please enter in whole number ==> {user_input}')  #print a warning sentence
    print(' --- program end --- ')                                 #print the last sentence
    quit()                                                         #Then quit the program
if time<3600:                                                      #Make a main condition if the time is less than 3600
    if time%60==0:    #When the main condition is true, try this 1st condition, if there is no remainder, there will be only minute, no more second
        print(f'{time:,} seconds ==> {int(minute):,} minutes')     #If 1st condition is true Then print the 'minutes'
    elif time%60!=0:                                               #else if try this 2nd condition, there will be extra second
        print(f'{time:,} seconds ==> {int(minute):,} minutes {second:,} seconds') #If 2nd condition is true, print it
elif time>=3600 and time<86400:  #It is the 2nd main condition, when the time is equal and between 3600 and (86400but not equal) because we want hour
    if time%3600==0:   #Like the previous explanation of the 1st condition
        print(f'{time:,} seconds ==> {int(hour):,} hours') #if the above condition is true, print it
    elif time%3600!=0: #Like the previous explanation of the 1st condition
        print(f'{time:,} seconds ==> {int(hour):,} hours {int(minute):,} minutes {int(second):,} seconds') #When the above condition is true,print it
elif time>=86400 and time<604800:   #It is the 3rd main condition, when the time is between 86400 and 604800 because we want day
    if time%86400==0:  #Like the previous explanation of the 1st condition
        print(f'{time:,} seconds ==> {int(day):,} days') #if the above condition is true, print the 'days'
    elif time%86400!=0: #Like the previous explanation of the 1st condition
        print(f'{time:,} seconds ==> {int(day):,} days {int(hour_in_a_day):,} hours {int(minute):,} minutes {int(second):,} seconds') #then print it
elif time>=604800:      #It is the 4th main condition, it will be ture when the time is equal and greater than 604800 becausewe want week
    if time%604800==0:  #Like the previous explanation of the 1st condition
            print(f'{time:,} seconds ==> {int(week):,} weeks') #If the above condition is true, then print it.
    elif time%604800!=0 and 0!=int(day_in_a_week) and 0!=int(hour_in_a_day) and 0==int(minute) and 0!=int(second):
            #Like the previous explanation of the 1st condition but now we don't want to print the 0minute.
            print(f'{time:,} seconds ==> {int(week):,} weeks {int(day_in_a_week):,} days {int(hour_in_a_day):,} hours {int(second):,} seconds')#print it
    if time%604800!=0 and int(hour_in_a_day)==0 and int(minute)==0:#Like the previous explanation of the 1st condition but now we just wanna week&sec
            print(f'{time:,} seconds ==> {int(week):,} weeks {int(second):,} seconds') #print the week and second when the above condition is true
print(' --- program end --- ')  #Print the last statement of the program