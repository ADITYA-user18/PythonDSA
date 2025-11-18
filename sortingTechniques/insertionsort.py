
n = [1,2,1,12,1,3,4,2,4,2,5,6,7,8,3,6,5,4]
for i in range(1,len(n)):
    key=n[i]
    j=i-1
    while j>=0 and n[j] > key:
        n[j+1]= n[j]
        j-=1
    n[j+1] = key

print(n)
    
