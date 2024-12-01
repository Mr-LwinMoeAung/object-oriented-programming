lists=[1,2,3,4,5]
max=lists[0]
second_largest=0
third=0
for com in lists:
    if com>max:
        max=third
        third=second_largest
        second_largest=com
        
print(third,second_largest,max)

print()

# lists=[1,9,7,5,0]
# max=lists[0]
# second_largest=0
# third=0
# fourth=0
# for com in lists:
#     if com>max:
#         max=fourth
#         fourth=third
#         third=second_largest
#         second_largest=com
        
# print(fourth,third,second_largest,max)