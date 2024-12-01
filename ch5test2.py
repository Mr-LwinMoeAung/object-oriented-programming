print(' *** Creating Dictionary ***')           #Print the header
user=input('Enter text : ')                     #Get the input from user
arr=[]                                          #Create an empty list
arr=user.split()                                #Then split the input into that list
dic={}                                          #Create an empty dictionary
list2=[]                                        #Create two empty lists
list1=[]
for i in range(len(arr)):                       #Loop for len(arr) times
    if i % 2 == 0:                              #Want to append the stuff at the even position
        list1.append(arr[i])                    #If at the even postion, append them
    else:                                       #else
        list2.append(int(arr[i]))               #Append to the next list
                                        #The length of list1 and 2 are the same and their related positions are also same
for x in range(len(list1)):                     #Nested loop to find the duplicate 
    for y in range(len(list1)):
        if list1[x]==list1[y] and x!=y and y>=x:    #Finding duplicates and keys from same position should not be same
            list2[x]=list2[x]+list2[y]       #If list1 have duplications stuff, the related position from list2 are added

for x in range(len(list1)):                     #Then same nested loop again
    for y in range(len(list1)):
        if list1[x]==list1[y] and x!=y:         #In dictionary, last value is assigned for a key
            list2[y]=list2[x]                   #So I make all the value to be the same 

for k in range(len(list1)):
    dic[list1[k]]=list2[k]                      #Then assign the related keys and values
print(dic)                                      #Print the answer