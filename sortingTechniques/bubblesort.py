


a = [1,3,45,5,6,7,2,4,5,67,7,8,7,4,3]
for i in range(len(a)):
 for j in range(len(a)-1):
    if a[j]>a[j+1]:
        a[j],a[j+1]=a[j+1],a[j]
print(a)