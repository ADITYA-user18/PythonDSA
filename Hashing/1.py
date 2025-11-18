a = [10,20,30,4,1,5,12,5,1,23,23,85,21,225,56,6,5]

b = [20,3,1,2,5,46,6,5,23]



for i in b:
    count = 0
    for j in a:
        if j == i:
            count +=1 
    print(count)
