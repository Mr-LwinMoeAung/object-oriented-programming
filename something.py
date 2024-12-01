# for i in range(65, 120):
#     j = (i - 65) % 26 + 65
#     print(i, ' : ', chr(j))


user=input('Enter numbers : ')
user_list=user.split()
print(user_list)
for i in range(len(user_list)):
    user_list[i]=int(user_list[i])
print(user_list)
new_list=user_list[:]
x=1
for z in range(len(user_list)):
    for i in range(len(user_list)):
        if z!=i:
            if user_list[z]==user_list[i]:
                new_list.remove(user_list[i])
                print(new_list)