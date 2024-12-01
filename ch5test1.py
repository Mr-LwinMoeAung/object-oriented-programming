print(' *** Creating Dictionary ***')
user=input('Enter text : ')
arr=[]
arr=user.split()
dic={}
for i in range(len(arr)):
    dic[arr[i*2]]=arr[(i*2)+1]
    if len(arr)/2==len(dic):
        break
print(dic)