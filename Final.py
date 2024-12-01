# class MyInt:
#     def __init__(self,value):
#         self.value=int(value)
#     def __add__(self,other):
#         rev=int(str(other.value)[::-1])
#         return f'{self.value} + {other.value} = {self.value} + {rev} = {self.value+rev}'
#     def __str__(self):
#         return f'{self.value}'
# class WeirdInt(MyInt):
#     def __add__(self,other):
#         revv=int(str(self.value)[::-1])
#         return f'{self.value} + {other.value} = {revv} + {other.value} = {revv+other.value}'

# print(" *** Weird Integer ***")
# a,b = input("Enter a b : ").split()
# a = MyInt(a)
# b = WeirdInt(b)
# print(f"{a} + {b} => {a+b}")
# print(f"{b} + {a} => {b+a}")

#  *** Weird Integer ***
# Enter a b : 12 36
# 12 + 36 => 12 + 36 = 12 + 63 = 75
# 36 + 12 => 36 + 12 = 63 + 12 = 75

# class MyInt:
#     def __init__(self,value):
#         self.value=int(value)
#     def __add__(self,other):
#         rev=int(str(other.value)[::-1])
#         return f'{self.value} + {rev} = {self.value+rev}'
#     def __sub__(self,other):
#         rev=int(str(other.value)[::-1])
#         return f'{self.value} - {rev} = {self.value-rev}'
#     def __str__(self):
#         return f'{self.value}'
    
# class WeirdInt(MyInt):
#     def __add__(self,other):
#         rev=int(str(self.value)[::-1])
#         revv=int(str(other.value)[::-1])
#         return f'{rev} + {revv} = {rev+revv}'
#     def __sub__(self,other):
#         rev=int(str(self.value)[::-1])
#         revv=int(str(other.value)[::-1])
#         return f'{rev} - {revv} = {rev-revv}'

# print(" *** Weird Integer II ***")
# a,b = input("Enter a b : ").split()
# a = MyInt(a)
# b = WeirdInt(b)
# print(f"{a} + {b} => {a+b}")
# print(f"{b} + {a} => {b+a}")
# print(f"{a} - {b} => {a-b}")
# print(f"{b} - {a} => {b-a}")

# Enter a b : 123 456
# 123 + 456 => 123 + 654 = 777
# 456 + 123 => 654 + 321 = 975
# 123 - 456 => 123 - 654 = -531
# 456 - 123 => 654 - 321 = 333





#  *** Creating Dictionary ***
# Enter text : apple 12 bamboo 19 grape 45 durian 120 apple 12 bamboo 19 grape 45
# {'apple': 24, 'bamboo': 38, 'grape': 90, 'durian': 120}


# user=input('Enter something : ')
# arr=user.split()
# print(arr)
# list1=[]
# list2=[]
# result_dict=[]
# for i,char in enumerate(arr):
#     if i%2==0:
#         list1.append(char)
#     else:
#         list2.append(int(char))

# print(list1) 
# print(list2)

# for i in range(len(list1)):
#     key=list1[i]
#     value=list2[i]

#     if key in result_dict:
#         result_dict[key] += value
#     else:
#         result_dict[key]=value

# print(result_dict)




# def create_dictionary_from_input():
#     user_input = input("Enter text: ").split()

#     dictionary = {}
#     i = 0
#     while i < len(user_input):
#         key = user_input[i]
#         value = int(user_input[i + 1])

#         if key in dictionary:
#             dictionary[key] += value
#         else:
#             dictionary[key] = value

#         i += 2
#     print(key,value)
#     return dictionary

# # Example usage
# result = create_dictionary_from_input()
# print(result)



# Enter : aabbcd abbccd
# dict1 = {'a': 2, 'b': 2, 'c': 1, 'd': 1}
# dict2 = {'a': 1, 'b': 2, 'c': 2, 'd': 1}
# Dictionaries comparison:
# b 2
# d 1




# user1,user2=input('Enter : ').split()

# dict1={}
# dict2={}

# for char in user1:
#         if char in dict1:
#             dict1[char]+=1
#         else:
#             dict1[char]=1
# for char in user2:
#         if char in dict2:
#             dict2[char]+=1
#         else:
#             dict2[char]=1

# print(dict1)
# print(dict2)

# intersection=dict1.items() & dict2.items()

# for key,value in sorted(intersection):
#      print(key,value)




# user1,user2=input('Enter : ').split()
# dict1={}
# dict2={}

# for i in user1:
#     if i in dict1:
#         dict1[i]+=1
#     else:
#         dict1[i]=1

# print(dict1)



#  *** Creating Dictionary ***
# Enter text : apple 12 bamboo 19 grape 45 durian 120 apple 12 bamboo 19 grape 45
# {'apple': 24, 'bamboo': 38, 'grape': 90, 'durian': 120}


# user=input('Enter : ').split()
# list1=[]
# list2=[]
# print(user)
# dictionary={}

# for i,char in enumerate(user):
#     if i%2==0:
#         list1.append(char)
#     else:
#         list2.append(int(char))

# for i in range(len(list1)):
#     if list1[i] in dictionary:
#         dictionary[list1[i]]+=list2[i]
#     else:
#         dictionary[list1[i]]=list2[i]

# print(dictionary)


# Enter : Ford 10 Toyota 10
# dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}
# Ford does not exist
# Toyota exists in dicts
# dict_new = {'Volkswagan': 1, 'Toyota': 12, 'Tesla': 2, 'Ford': 10}

# user=input('Enter : ').split()
# list1=[]
# list2=[]
# dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}

# for i,char in enumerate(user):
#     if i%2==0:
#         list1.append(char)
#     else:
#         list2.append(int(char))

# for i in range(len(list1)):
#     if list1[i] in dict_old:
#         dict_old[list1[i]]+=list2[i]
#     else:
#         dict_old[list1[i]]=list2[i]

# print(dict_old)

# *** Shopping List 2 ***
# Enter some pairs of (operation, item): a wagyu,a salmon,r ham
# Final shopping dict is {'egg': 1, 'water': 1, 'soda': 1, 'wagyu': 1, 'salmon': 1}


# shopping_dict = {
#     "egg": 1,
#     "ham": 1,
#     "water": 1,
#     "soda": 1,
# }
# user=input('Enter : ').split(',')
# print(user)
# list1=[]
# list2=[]

# for i in user:
#     operation,item=i.strip().split()
#     list1.append(operation)
#     list2.append(item)
#     if operation!='a' and operation!='r':
#         print('Operation not allow')
#         exit()

# print(list1)
# print(list2)

# for i in range(len(list1)):
#     if 'a' in list1[i]:
#         if list2[i] in shopping_dict:
#             shopping_dict[list2[i]]+=1
#         else:
#             shopping_dict[list2[i]]=1
#     elif 'r' in list1[i]:
#         if list2[i] in shopping_dict:
#             shopping_dict.pop(list2[i])

# print(shopping_dict)



# *** Shopping List 2 ***
# Enter some pairs of (operation, item): a wagyu,a salmon,r ham
# Final shopping dict is {'egg': 1, 'water': 1, 'soda': 1, 'wagyu': 1, 'salmon': 1}

def isPrime(x):
    if x<2:
        return False
    for i in range(2,x):
        if x%i==0:
            return False
    return True
def show(x):
    prime=[]
    k=''
    for i in range(2,x):
        if isPrime(i):
            prime.append(i)
    for i in range(len(prime)):
        k+=str(prime[i])+' '
    return k




print(isPrime(5))
print(show(5))