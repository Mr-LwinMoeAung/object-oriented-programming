def is_prime(n):                                        #Make a function
    if n < 2:                                           #Not to greater than 2
        return False                                    #if that happen, it is false
    for i in range(2, n):                               #A loop to get prime number
        if n % i == 0:                                  #If this calculation is true
            return False                                #Just return false
    return True                                         #else return true and we get prime numbers

print(' *** Convert every prime character ***')         #Header
user = input("Enter any string : ")                     #Get the input
new = ""                                                #Declare an empty string
for i, char in enumerate(user):                         #Tried to do with enumerate according to the lecture
    if is_prime(i+1):                                   #If the function return true
        if char.islower():                              #Checking lower?
            new += char.upper()                         #Put it in the empty string then change it to upper
        else:                                           #else
            new += char.lower()                         #Put it in the empty string then change it to lower
    else:                                               #if it is not prime number
        new += char                                     #Just put the original character

print(f"{user} ==> {new}")                              #Print the result
print("===== End of program =====")                     #End