dic={
    'ball':'red',
    'bat':4,
    'wickets':8,
    'ball':'green',
    'bat':3
    }
empty= []
var = dict() 
for key, value in dic.items(): 
    if value not in empty and key not in empty:
        empty.append(key)
        empty.append(value)
        var[key] = value
print(var2)
# print(empty)
  
# for i in dic:
#     for k in dic:
#         if k not in empty:
#             empty.append(k)
#             var[i]=k
# print(empty)

