n1 = [1,5,4,8,7,5]
n2 = [2,6,8,3,1,5]
res=[]
dict={}

for n in n1:
    if n not in dict:
        dict[n]=1
    else:
        dict[n]+=1


for num in n2:
    if num in dict and dict[num] > 0:
        res.append(num)
print(res)