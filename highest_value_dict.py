dict={1:12,2:14,3:16,4:18,5:19}
max1=0
max2=0
max3=0
empty=[]
for i in dict:
    for k in dict:
        if dict[i]>max1:
            max1=dict[i]
        elif max1>dict[k] and max2<dict[k]:
            max2=dict[k]
        elif max2>dict[k] and max3<dict[k]:
            max3=dict[k]
empty.append(max1)
empty.append(max2)
empty.append(max3)
print(empty)
        
        
