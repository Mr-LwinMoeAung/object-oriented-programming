# class Stack:
#     def __init__(self):
#         self.box=list()
#         self.box1=list()

#     def push(self,a):
#         self.box.append(a)

#     def pop(self):
#         self.box1.append(self.box.pop())

#     def peek(self):
#         return self.box[0]

#     def size(self):
#         return len(self.box)

#     def __str__(self):
#         ans=''
#         for i in self.box1:
#             ans+=i+''
#         return ans

# Use=Stack()
# inp=input('Enter str: ')
# for i in inp:
#     Use.push(i)
# for i in range(len(inp)):
#     Use.pop()

# print(Use)



# class Stack:
#     def __init__(self):
#         self.box=''

#     def push(self,data):
#         self.box+=data
    
#     def pop(self):
#         while True:
#             if '()' in self.box:
#                 self.box=self.box.replace('()','')
#             elif '{}' in self.box:
#                 self.box=self.box.replace('{}','')
#             elif '[]' in self.box:
#                 self.box=self.box.replace('[]','')
#             else:
#                 return self.box

#     def __str__(self):
#         return f'{self.box}'
                
# use=Stack()
# inp=input('Enter : ')

# for i in inp:
#     if i in '({[]})':
#         use.push(i)
# use.pop()

# print(use)


# class Stack:
#     def __init__(self):
#         self.box=[]

#     def push(self,data):
#         self.box.append(data)

#     def pop(self):
#         for i in self.box:
#             if isinstance(i,str):
#                 check=self.box.index(i)
#                 first=check-2
#                 second=check-1
#                 a=self.box[first]
#                 b=self.box[second]
#                 ans=eval(f'{a} {i} {b}')
#                 self.box[check]=ans
#                 self.box[first]='@'
#                 self.box[second]='@'

#     def __str__(self):
#         while '@' in self.box:
#             self.box.remove('@')
#         return f'{self.box}'

# use=Stack()
# inp=input('Enter: ').split()

# for i in inp:
#     try:
#         i=int(i)
#     except:
#         i=i
#     use.push(i)

# use.pop()
# print(use)



# class Stack:
#     def __init__(self):
#         self.box=[]

#     def push(self, item):
#         self.box=item

#     def pop(self):
#         count=1
#         for i in range(len(self.box)):
#             for j in range(len(self.box)):
#                 if i!=len(self.box)-1:
#                     j=i+count
#                     count+=1
#                 if self.box[i]<self.box[j]:
#                     self.box[i]=self.box[j]
#                     count=1
#                     break


# def find_next_greater_elements(arr):
#     stack = Stack()
#     result = []
#     result=arr.copy()
#     stack.push(result)
#     stack.pop()
#     return result


# # Test the function
# print(" *** Next Greater Element ***")
# inp = input("Enter list of number : ")
# inp = [int(ele) for ele in inp.split()]
# print(inp)
# next_greater = find_next_greater_elements(inp)
# print(next_greater)


#_______________________
#  *** Basic Linked List ***
# Enter data : 1 2 3
# 0 => [[Empty Linked List]]
# 1 => [[ 1]]
# 2 => [[ 1, 2]]
# 3 => [[ 1, 2, 3]]
#  ===== End of program =====


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def size(self):
#         return 0
    
#     def __str__(self):
#         result=[]
#         current=self.head

#         if self.head is None:
#             return 'Empty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#             return f'{", ".join(map(str,result))}'


# print(" *** Basic Linked List ***")
# inp = input("Enter data : ")
# myList = LinkedList()
# print(f"{myList.size()} => {myList}")
# for d in inp.split():
#     myList.append(d)
#     print(f"{myList.size()} => {myList}")
# print(" ===== End of program =====")


# class Node:
#     def __init__(self,data,next=None):
#         self.data = data
#         self.next = next
    
# class LinkedList:
#     def __init__(self):
#         self.head = None
    
#     def addHead(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node

#     def append(self,data):
#         new_node=Node(data)
#         current=self.head
#         if current is None:
#             self.head=new_node
#         else:
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node
    
#     def size(self):
#         count=0
#         current=self.head
#         while self.head is not None:
#             count+=1
#             current=current.next
#         return count
    
#     def __str__(self):
#         current=self.head
#         result=[]
#         if current is None:
#             return 'Empty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#             return f'{", ".join(map(str,result))}'
   
# print(" *** Basic Linked List ***")
# inp = input("Enter data : ")
# myList = LinkedList()
# print(f"{myList.size()} => {myList}")
# for index, data in enumerate(inp.split()):
#     if index%2 == 0:
#         myList.append(data)
#     else:
#         myList.addHead(data)
#     print(f"{myList.size()} => {myList}")

# print(" ===== End of program =====")


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         new_node=Node(data)
#         current=self.head
#         if current is None:
#             self.head=new_node
#         else:
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def __add__(self,other):
#         return f'{self.foradd}, {other.foradd}'
            
#     def __str__(self):
#         current=self.head
#         result=[]

#         if current is None:
#             return 'Empty'
        
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next        
#             self.foradd=f'{", ".join(map(str,result))}'
#             return f'{", ".join(map(str,result))}'

# print(" *** Linked List ADD ***")
# l1,l2 = input("Enter myList1 / myList2 : ").split('/')
# myList1 = LinkedList()
# myList2 = LinkedList()
# for index, data in enumerate(l1.split()):
#     myList1.append(data)
# for index, data in enumerate(l2.split()):
#     myList2.append(data)
# print(f"myList1 => {myList1}")
# print(f"myList2 => {myList2}")
# print(f"myList1 + myList2 => {myList1+myList2}")
# print(f"myList2 + myList1 => {myList2+myList1}")
# print(" ===== End of program =====")

# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node

#     def __str__(self):
#         result=[]
#         current=self.head
#         # if current is None:
#         #     return current.data
#         # else:
#         while current is not None:
#                 result.append(current.data)
#                 current=current.next
#         return f'{", ".join(map(str,sorted(result)))}' 

# class sortedLinkedList(LinkedList):
#     ''' Ascending order Linked List '''
#     def append(self,ele):
#         return super().append(ele)
        

# print(" *** Sorted Linked List ***")
# inp = input("Enter data : ")
# myList1 = sortedLinkedList()
# for index, data in enumerate(inp.split()):
#     num = int(data)
#     myList1.append(data)
#     print(f"{index+1}. add {num} => {myList1}")

# print(f"myList1 => {myList1}")

# print(" ===== End of program =====")

# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,data):
#         new_node=Node(data)
#         current = self.head
#         if current is None:
#             self.head=new_node
#         else:
#             while current.next is not None:
#                 current = current.next
#             current.next=new_node

#     def remove(self,ele):
#         if self.head is None:
#             return
#         if ele==self.head.data:
#             self.head=self.head.next
#             return
#         current=self.head
#         while current.next is not None:
#             if ele==current.next.data:
#                 break
#             current= current.next
#         if current.next is None:
#             return
#         else:
#             current.next=current.next.next


#     def __str__(self):
#         result=[]
#         current = self.head
#         if current is None:
#             return 'Empty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current = current.next

#             return f'{", ".join(map(str,result))}'
        
# class sortedLinkedList(LinkedList):
#     def append(self,ele):
#         return super().append(ele)
    
# print(" *** Sorted Linked List (remove) ***")
# inp = input("Enter data / remove-data : ")
# data, rData = inp.split('/')
# myList = sortedLinkedList()
# for index, data in enumerate(data.split()):
#     num = int(data)
#     myList.append(data)
#     # print(f"{index+1}. add {num} => {myList}")
# print(f"myList => {myList}")
# for index, data in enumerate(rData.split()):
#     num = int(data)
#     myList.remove(data)
#     print(f"{index+1}. remove {num} => {myList}")

# print(f"myList => {myList}")

# print(" ===== End of program =====")



# class Queue:
#     def __init__(self):
#         self.item = list()

#     def enqueue(self,data):
#         self.item.append(data)

#     def dequeue(self):
#         self.item.pop(0)

#     def size(self):
#         return len(self.item)
    
#     def __str__(self):
#         return f'{self.item}'

# print(" *** Basic Queue ***")
# items = input("Enter items : ").split()
# print(f"items={items}")
# q = Queue()
# for idx,ele in enumerate(items):
#     print(f"{idx+1} = {ele}")
#     q.enqueue(ele)
#     print(f"size={q.size()} => {q} ")
# print(" ===== End of program =====")


#  *** Basic Queue enqueue/dequeue***
# Enter items / n : 1 2 3 4 5 6 7 8 / 3
# items = 1 2 3 4 5 6 7 8 
# n = 3
# q1 => [['1', '2', '3', '4', '5', '6', '7', '8']]

# q1 => [['4', '5', '6', '7', '8']] 
# q2 = [['1', '2', '3']]
#  ===== End of program =====


# class Queue:
#     def __init__(self):
#         self.box=[]
#         self.n=int(n)

#     def enqueue(self,ele):
#         self.box.append(ele)

#     def dequeue(self):
#         return self.box.pop(0)

#     def size(self):
#         return len(self.box)

#     def __len__(self):
#         return self.n
    
#     def __str__(self):
#         return f'{self.box}'

# print(" *** Basic Queue enqueue/dequeue***")
# items,n = input("Enter items / n : ").split('/')
# print(f"items = {items}")
# print(f"n = {n.strip()}")
# q1 = Queue()
# q2 = Queue()
# for idx,ele in enumerate(items.split()):
#     # print(f"{idx+1} = {ele}")
#     q1.enqueue(ele)
# print(f"q1 => {q1}\n")
# for _ in range(len(q1)):
#     item = q1.dequeue()
#     q2.enqueue(item)
#     if q2.size() >= int(n):
#         break
# print(f"q1 => {q1} ")
# print(f"q2 = {q2}")

# print(" ===== End of program =====")

# class queue:
#     def __init__(self):
#         self.box=[]

#     def enqueue(self,ele):
#         self.box.append(ele)

#     def dequeue(self):
#         return self.box.pop(0)
    
#     def isEmpty(self):
#         return len(self.box)==0

#     def first(self):
#         if self.isEmpty()==False:
#             return self.box[0]
        
#     def last(self):
#         if self.isEmpty()==False:
#             return self.box[-1]

#     def size(self):
#         return len(self.box)

#     def __str__(self):
#         ans=''
#         for i in self.box:
#             ans+=i+' '
#         if self.size()!=0:
#             return f'Data in queue is : {ans}'
#         else:
#             return f'Data in queue is : EMpty'
# print(' *** Basic Queue 3 ***')
# inp=input('Enter Input : ').split(',')
# print(f'inp={inp}')
# q1=queue()

# for i in inp:
#     comamnd = i[:2].upper()
#     if comamnd == "EN":
#         data = i[3:].strip()
#         q1.enqueue(data)
#     elif comamnd == "DE":
#         q1.dequeue()
#     elif comamnd == "IE":
#         print("Queue empty = {0}".format(q1.isEmpty()))
#     elif comamnd == "SI":
#         print("Queue size = {0}".format(q1.size()))
#     elif comamnd == "FI":
#         print("First of queue = {0}".format(q1.first()))
#     elif comamnd == "LA":
#         print("Last of queue = {0}".format(q1.last()))
#     elif comamnd == "PR":
#         print(q1)

# print(' ===== End of program =====')


# class Queue:
#     def __init__(self):
#         self.box=[]
#         self.check=0
#     def enqueue(self,ele):
#         self.box.append(ele)

#     def dequeue(self):
#         return self.box.pop(0)
    
#     def size(self):
#         self.check+=1
#         return f'{self.check:2}'
    
#     def __len__(self):
#         return len(self.box)

#     def __str__(self):
#         return f'{self.box}'


# print(' *** Queue Journey ***')
# inp=input('Enter people : ').split('-')
# main=Queue()
# q1=Queue()
# q2=Queue()
# count=0

# print('minute => [ Main Queue ] == [ Queue-1 ] == [ Queue-2]')
# count=0
# for i in inp:
#     main.enqueue(i)

# for i in range(len(main)):
#     count+=1
#     mainpop=main.dequeue()
#     if count==4:
        
#     if count<=3:
#         q1.enqueue(mainpop)

#     print(f'{main.size()} => {main} == {q1} == {q2}')


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,ele):
#         new_node=Node(ele)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current= self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def size(self):
#         current=self.head
#         count=0
#         while current is not None:
#             current=current.next
#             count+=1
#         return count

#     def __str__(self):
#         if self.head is None:
#             return 'Empty'
#         else:
#             result=[]
#             current=self.head
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#             return f"{' ,'.join(map(str,result))}"

# inp=input('Enter : ').split()
# l=LinkedList()

# print(f"{l.size()} => {l}")

# for i in inp:
#     l.append(i)
#     print(f"{l.size()} => {l}")
# print(" ===== End of program =====")



# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,ele):
#         new_node=Node(ele)
#         new_node.next=self.head
#         self.head=new_node

#     def addHead(self,ele):
#         new_node=Node(ele)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def size(self):
#         current=self.head
#         count=0
#         while current is not None:
#             current=current.next
#             count+=1
#         return count
    
#     def __str__(self):
#         current=self.head
#         result=[]
#         if current is None:
#             return 'Empty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#             return f"{' ,'.join(map(str,result))}"

# print(" *** Basic Linked List ***")
# inp = input("Enter data : ")
# myList = LinkedList()
# print(f"{myList.size()} => {myList}")
# for index, data in enumerate(inp.split()):
#     if index%2 == 0:
#         myList.append(data)
#     else:
#         myList.addHead(data)
#     print(f"{myList.size()} => {myList}")

# print(" ===== End of program =====")

# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,ele):
#         new_node=Node(ele)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def __add__(self,other):
#         return self.for_add +','+ other.for_add

#     def __str__(self):
#         current=self.head
#         result=[]
#         if current is None:
#             return 'Empty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#                 self.for_add=f"{','.join(map(str,result))}"
#             return f"{','.join(map(str,result))}"


# print(" *** Linked List ADD ***")
# l1,l2 = input("Enter myList1 / myList2 : ").split('/')
# myList1 = LinkedList()
# myList2 = LinkedList()
# for index, data in enumerate(l1.split()):
#     myList1.append(data)
# for index, data in enumerate(l2.split()):
#     myList2.append(data)
# print(f"myList1 => {myList1}")
# print(f"myList2 => {myList2}")
# print(f"myList1 + myList2 => {myList1+myList2}")
# print(f"myList2 + myList1 => {myList2+myList1}")
# print(" ===== End of program =====")


# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,ele):
#         new_node=Node(ele)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def __str__(self):
#         current=self.head
#         result=[]
#         if current is None:
#             return 'Empty'
        
#         while current is not None:
#             result.append(current.data)
#             current=current.next
#         return f"{','.join(map(str,sorted(result)))}"


# class sortedLinkedList(LinkedList):
#     ''' Ascending order Linked List '''
#     def append(self,ele):
#         super().append(ele)
    
# print(" *** Sorted Linked List ***")
# inp = input("Enter data : ")
# myList1 = sortedLinkedList()
# for index, data in enumerate(inp.split()):
#     num = int(data)
#     myList1.append(data)
#     print(f"{index+1}. add {num} => {myList1}")
# print(f"myList1 => {myList1}")

# print(" ===== End of program =====")

# class Node:
#     def __init__(self,data,next=None):
#         self.data=data
#         self.next=next

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def append(self,ele):
#         new_node=Node(ele)
#         current = self.head
#         if current is None:
#             self.head=new_node
#         else:
#             while current.next is not None:
#                 current=current.next
#             current.next=new_node

#     def remove(self,ele):
        
#         if self.head is None:
#             return
#         if self.head.data==ele:
#             self.head=self.head.next
#             return
#         current=self.head
#         while current.next is not None:
#             if current.next.data==ele:
#                 break
#             current=current.next
#         if current.next is None:
#             return
#         else:
#             current.next=current.next.next

#     def __str__(self):
#         result=[]
#         current=self.head
#         if current is None:
#             return 'EMpty'
#         else:
#             while current is not None:
#                 result.append(current.data)
#                 current=current.next
#             return f"{','.join(map(str,sorted(result)))}"


# class sortedLinkedList(LinkedList):
#     ''' Ascending order Linked List '''
#     def append(self,ele):
#         return super().append(ele)
#     def remove(self,ele):
#         return super().remove(ele)

# print(" *** Sorted Linked List (remove) ***")
# inp = input("Enter data / remove-data : ")
# data, rData = inp.split('/')
# myList = sortedLinkedList()
# for index, data in enumerate(data.split()):
#     num = int(data)
#     myList.append(data)
#     # print(f"{index+1}. add {num} => {myList}")
# print(f"myList => {myList}")
# for index, data in enumerate(rData.split()):
#     num = int(data)
#     myList.remove(data)
#     print(f"{index+1}. remove {num} => {myList}")

# print(f"myList => {myList}")

# print(" ===== End of program =====")




# def fibo(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(7))


# def leng(n):
#     if n=='':
#         return 0
#     else:
#         return 1+leng(n[1:])
    
# def add(a,b,i=0):
#     if i==b:
#         return
#     elif i<=b:
#         if i%2==0:
#             print(a[i]+'~',end='')
#             add(a,b,i+1)
#         else:
#             print(a[i]+'*',end='')
#             add(a,b,i+1)

# ans=leng('lwin')
# print(ans)
# add('lwin',ans)



# def bi(n,current=''):
#     if n==0:
#         print(current)
#     else:
#         bi(n-1,current+'0')
#         bi(n-1,current+'1')

# bi(3)


# def stair(n,a=1):
#     if n==0:
#         return
#     elif n>=a:
#         print('#'*(n-a)+'*'*a)
#         stair(n,a+1)
# stair(5)

# def test(n,count=0):
#     if len(n)==1:
#         return n
#     else:
#         return test(n[1:])+n[0]
# print(test('abc'))