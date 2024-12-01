print('*** Shopping List 2 ***')

shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}

user=input('Enter some pairs of (operation, item): ')   #Get the input from user
list1=user.split(',')                                   #Split at the ','
list2=[]                                                #Declare an empty list

for i in list1:                                         
    list2.append(i.split())                             #Split them and append the list into the list
                                                        #So, List2 is a list in a list
for i in list2:                                         #Call out the list from list2
    if 'a' not in i and 'r' not in i:                   #If other characters except 'a' and 'r'
        print('Operation not supported!')               #Print and 
        exit()                                          #End the program

    x=i[1]                              #There will be only two length for the inner list, then I name the last one

    if 'a' in i:                        #Find 'a' in the inner list
        if x in shopping_dict:          #Find the same keys in shopping_dict
            shopping_dict[x]+=1         #If found, just need to plus one to the original one
        else:                           #If not found
            shopping_dict.update({x:1}) #Need to update for the new key and its new value
    if 'r' in i:                        #If found 'r'
        shopping_dict.pop(x)            #Just need to pop it

print(f'Final shopping dict is {shopping_dict}')    #Print the result