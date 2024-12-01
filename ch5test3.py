user=input('Enter : ')      #Get the input from user
user1,user2=user.split()    #Split the input 
list1=[]                    #Creating lists
list2=[]
new1=[]
new2=[]
count = []
count2=[]
dict1={}
dict2={}
num=0
num2=0

for i in user1:
    list1.append(i)         #Append the first string 

for j in user2:
    list2.append(j)         #Append the second string

for i in list1:
    if i not in new1:       #Remove the duplicates
        new1.append(i)      

for i in list2:
    if i not in new2:       #Remove the duplicates
        new2.append(i)

for x in range(len(new1)):          #Create the nested loop
    for y in range(len(list1)):
        if new1[x] in list1[y]:     #Find the number of count of duplicates from first string
            num+=1                  #Counting the numbers
    count.append(num)               #Then append them into a new list
    num=0

for x in range(len(new2)):          #Same as previous nested loop
    for y in range(len(list2)): 
        if new2[x] in list2[y]:     #But this one is for the second string
            num2+=1
    count2.append(num2)
    num2=0

for i in range(len(new1)):          #Loop it
    dict1[new1[i]]=count[i]         #Then assign the dictionary for the first string's stuff
print (f'dict1 = {dict1}')          #Printing

for i in range(len(new2)):          #Same as above 
    dict2[new2[i]]=count2[i]        
print (f'dict2 = {dict2}')

intersection=dict1.items() & dict2.items()      #Find the intersection between two dictionary

print('Dictionaries comparison:')               #Printing

if len(intersection)==0:                        #If the length of intersection is zero, there is no intersection
    print('None')                               #If ture, then print

for key, value in sorted(intersection):         #Loop to print key and value inside of sorted intersection
    print(key, value)#Then print, the reason I used sorted is, the key and value are swapping every single time when I run