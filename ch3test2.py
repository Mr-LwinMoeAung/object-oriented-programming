print(' *** Adding two lists ***')                  #Header
user=input('Enter list1 / list2 : ')                #Getting input
user_list1,user_list2=user.split(' / ')             #Split in '/'
user_list1=user_list1.split(' ')                    #Split in 'Space'
user_list2=user_list2.split(' ')                    #same
lists=[]                                            #empty list
for i in range(len(user_list1)):                    #Loop to change integer type
    user_list1[i]=int(user_list1[i])
print(f'List1 = {user_list1}')                      #Print the result
for i in range(len(user_list2)):                    #same
    user_list2[i]=int(user_list2[i])                
print(f'List2 = {user_list2}')                      
if len(user_list1)>len(user_list2):                 #if the first list length is greater than second
    minus1=len(user_list1)-len(user_list2)          #Get the extra length from list 1
    for i in range(minus1):                         #loop in it
        user_list2.append(0)                        #To make calculation, we need to put '0' at the end of the array
    for i in range(len(user_list1)):                #Loop to make calculation
        ans=user_list1[i]+user_list2[i]             #Summation
        lists.append(ans)                           #Then append the ans in the list
    print(f'ListNew = {lists}')                     #Print the result
elif len(user_list1)<len(user_list2):               #Same process  checking list2 may greater than 1
        minus2=len(user_list2)-len(user_list1)      
        for i in range(minus2):
            user_list1.append(0)
        for i in range(len(user_list2)):
            ans=user_list1[i]+user_list2[i]
            lists.append(ans)
        print(f'ListNew = {lists}')
elif len(user_list1)==len(user_list2):              #Same process  checking are they equal?
        for i in range(len(user_list1)):
            ans=user_list1[i]+user_list2[i]
            lists.append(ans)
        print(f'ListNew = {lists}')                 #Print the result