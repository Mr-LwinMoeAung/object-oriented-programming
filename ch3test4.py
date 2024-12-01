print(' *** Remove all occurences from a to b ***') #Print the header
user=input('Enter a b / list : ')                   #Getting input
user1,lists=user.split(' / ')                       #Split in /
a,b=user1.split(' ')                                #Split in space
lists=lists.split(' ')
a, b = int(a), int(b)                               #Change to integer

for i in range(len(lists)):                         #Loop to change integer from array
    lists[i]=int(lists[i])                          
print(f'old list =',lists)                          #Print the old list

new_lst = []                                        #Declare the empty list

for num in lists:                                   #Want to call out each integer from an array
    if num < a or num > b:                          #Then compare it with the a,b
        new_lst.append(num)                         #If ture, append them to the empty array
print(f'new list =',new_lst)                        #Printing the result