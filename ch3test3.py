print(' *** Swap first and last character ***') #Header
user=input('Enter words : ')                    #Getting input
user1=user.split( )                             #split it
box=[]                                          #Declare the empty array
box=user1                                       #Equal with user1

for j in range(len(box)):                       #Loop
    plus=0                                      #To make increasement
    x=len(box[j])-1                             #To reverse the last character
    print(x)
    print(box[j])
    ans=box[j]                                  #I wanted to the code to look better , box[j][0] = ans[0] just like this
    print(ans[x],end='')                        #Print the last character first 
    for i in range(len(box[j])-2):              #To make reverse order for the middle characters
        if plus<len(box[j]):                    #Just only want to make increasement if plus is less than len(box[j])
            plus+=1                             #if true , make increasement
        print(ans[plus],end='')                 #print the result
    print(ans[0],'',end='')                     #Print the first character at the last of it
print()
print('===== End of program =====')             #End