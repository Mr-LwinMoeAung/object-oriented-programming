# user=input('Enter : ')
# x=user.split()
# list1=[]
# list2=[]
# dic={}

# for i,char in enumerate(x):
#     if i%2==0:
#         list1.append(char)
#     else:
#         list2.append(char)

# for i in range(len(list1)):
#     dic[list1[i]]=list2[i]

# print(dic)




# user=input('Enter : ')
# x=user.split()
# list1=[]
# list2=[]
# dic={}

# for i,char in enumerate(x):
#     if i%2==0:
#         list1.append(char)
#     else:
#         list2.append(int(char))

# print(list1)
# print(list2)
# dic={}
# new=[]

# for i in range(len(list1)):
#     for j in range(len(list1)):
#         if list1[i]==list1[j] and i!=j and i<=j:
#             list2[j]=list2[i]+list2[j]
#             print(list2)
  
# print(list2)

# for k in range(len(list1)):
#     dic[list1[k]]=list2[k]

# print(dic)



# user=input('Enter : ')
# a,b=user.split()
# list1=[]
# list2=[]
# new1=[]
# new2=[]
# kk=[]
# kk1=[]
# dic1={}
# dic2={}
# count1=0
# count=0

# for i in a:
#     list1.append(i)
# print(list1)
# for i in b:
#     list2.append(i)
# print(list2)

# for j in list1:
#     if j not in new1:
#         new1.append(j)

# for j in list2:
#     if j not in new2:
#         new2.append(j)

# for x in range(len(new1)):
#     for y in range(len(list1)):
#         if new1[x] in list1[y]:
#             count+=1
#     kk.append(count)
#     count=0
# for x in range(len(new2)):
#     for y in range(len(list2)):
#         if new2[x] in list2[y]:
#             count1+=1
#     kk1.append(count1)
#     count1=0

# print(kk)
# print(kk1)

# print(new1)
# print(new2)

# for i in range(len(new1)):
#     dic1[new1[i]]=kk[i]
# for i in range(len(new2)):
#     dic2[new2[i]]=kk1[i]

# print(dic1)
# print(dic2)

# intersection= dic1.items() & dic2.items()
# print(sorted(intersection))



# dict_old={'Volkswagan': 1, 'Toyota': 2, 'Tesla':2}
# dict_new=dict_old.copy()
# dic={}
# list1=[]
# list2=[]

# user=input('Enter : ')
# lists=user.split()
# print(dict_old)

# for i,j in enumerate(lists):
#     if i%2==0:
#         list1.append(j)
#     else:
#         list2.append(int(j))

# for i in range(len(list1)):
#     if list1[i] in dict_new:
#         print(f'{list1[i]} exists')
#         value=dict_new[list1[i]]+list2[i]
#         dict_new.update({list1[i]:value})
#     else:
#         print(f'{list1[i]} does not exist')
#         dict_new.update({list1[i]:list2[i]})

# print(dict_new)

shopping_dict={'egg':1,'ham':1,'water':1,'soda':1}
user=input('Enter : ').split(',')
list1=[]
list2=[]

for i in user:
    list1.append(i[0])
    list2.append(i[2:])


for i in list1:
    if 'a' != i and 'r' != i:
        print('Operation not support!')
        exit()

for i in range(len(list2)):
    if list1[i]=='a':
        if list2[i] in shopping_dict:
            shopping_dict[list2[i]]+=1
        else:
            shopping_dict.update({list2[i]:1})
    if list1[i]=='r':
        shopping_dict.pop(list2[i])

print(shopping_dict)