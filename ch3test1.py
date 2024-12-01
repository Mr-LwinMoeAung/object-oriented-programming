print(' *** Remove Duplicate ***')          #Printing Header
user = input('Enter numbers : ')            #Getting input
user_list = user.split()                    #Splited it
x_list=[]                                   #Declare new empty array
new_list = []                               #Declare another new empty array
sum_of_duplicates = 0                       #To make summation
for x in user_list:                         #loop it
    x = int(x)                              #Change it to integer type
    if x not in new_list:                   #checking
        new_list.append(x)                  #if true, append it in the empty list
    else:                                   #else
        sum_of_duplicates += x              #Just make summation
        x_list.append(x)                    #Put it in the another empty list
print(f"newList = {new_list}")              #Print the answer
print('sum of duplicate = ',end='')         #Print the answer
for i in range(len(x_list)):                #Loop to print the process of summation
    print(x_list[i],end='')             
    if len(x_list)-1>i:
        print('+',end='')
if sum_of_duplicates!=0:
    print(f' = {sum_of_duplicates}')
else:
    print(sum_of_duplicates)                #not to print extra '='
print("===== End of program =====")         #End