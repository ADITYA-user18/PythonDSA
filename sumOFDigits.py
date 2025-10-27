list = [1,2,5,4,5]

found = False
target = 10

for i in range(len(list)):
    for j in range(i + 1 , len((list))):

        if list[i] + list[j] == target:
            found = True

           
print(found)

           








        