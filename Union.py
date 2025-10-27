n1 = [1,5,4,8,7,5,3]
n2 = [2,6,5,8,3]
res=[]

for  num in n1+n2:
    if num not in res:
        res.append(num)
print(res)