dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}   #Old dictionary
dict_new=dict_old.copy()                                #New dictionary copied the old
user=input('Enter : ')                                  #Get input from user
list1=user.split()                                      #Then split the user inputer directly into a list
item=[]                                                 #Declare the empty list
val=[]                                                  #Same
new=0

for i in range(len(list1)):                             #Looping
    if i%2==0:                                          #Get the stuff from even position
        item.append(list1[i])                           #Then append them
    else:                                               #Get the stuff from odd position
        val.append(int(list1[i]))                       #Then append them

print(f'dict_old = {dict_old}')                         #Print the old dictionary
for j in range(len(item)):                              #Loop
        if item[j] in dict_old:                         #Find the input in the old one
            print(f'{item[j]} exists in dicts')         #If exist, print
            key=item[j]                                 #Naming
            value=val[j]                                #Naming
            new+=value                                  #Plus the incoming values to new
            ans=new+dict_old[key]                       #Add existed original one and new one
            dict_new.update({key:ans})                  #Then update the related key and value of dictionary
        else:                                           #If the input does not exist in the old dictionary
            print(f'{item[j]} does not exist')          #Print it
            dict_new.update({key:value})           #Print the (Not existed stuffs) and (Existed stuff) together
            
if len(dict_new)==3:                           #If there is no new incoming things,The lenght of dictionary will be three
    dict_old.update({key:ans})                  #Then update the original dictionary with the new values
    print(f'dict_new = {dict_old}')             #Then print the old one
else:                                           #If the length is changed, it will be new one
    print(f'dict_new = {dict_new}')             #Then print the new one