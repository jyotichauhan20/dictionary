my_dict = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    }
max1=0
max2=0
max3=0
empty=[]
for i in my_dict:
    for k in my_dict:
        if my_dict[i]>max1:
            max1=my_dict[i]
        elif max1>my_dict[k] and max2<my_dict[k]:
            max2=my_dict[k]
        elif max2>my_dict[k] and max3<my_dict[k]:
            max3=my_dict[k]
empty.append(max1)
empty.append(max2)
empty.append(max3)
print(empty)
        
        
