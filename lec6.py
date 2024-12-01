# mlist=[1,2,3,4,5,6,7,1,4,5,7]
# mSet=set(mlist)
# print('Set is = ',mSet)

mSet1 = {11,12,13,14,15}
mSet2= {11,12,6,7,8}

print(mSet1.intersection(mSet2))
mSet3={}
mSet4=set()
print(type(mSet3),type(mSet4))

mlist=[11,12,13]
print(mlist[0])
mDict={'class': "oop", 'room' : 'ce706', 0:7}
print(mDict)
print(len(mDict))
print(mDict[0])
for x in mDict:
    print(x, ' => ',mDict[x])

x=(1,2,3,11,13)
print('x=>',x)
print(type(x))