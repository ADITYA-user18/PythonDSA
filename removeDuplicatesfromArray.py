arr =  [1,2,4,8,7,5,6,1,2,4,5,2,3,6,2,5,5,10,11,12,14,11]


dict={}
duplicates=[]


for val in arr:
    if val in  dict:
        dict[val]+=1
    else:
        dict[val]=1

for key in dict:
    if dict[key]>1:
        duplicates.append(key)

print(duplicates)










