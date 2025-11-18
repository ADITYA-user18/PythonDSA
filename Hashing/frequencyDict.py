list = [12,20,14,1,20,14,1,3,5,6,3,6,2,8,9,9]

dict  = {}

for i in range (len(list)):
    if list[i] in dict:
        dict[list[i]] += 1
    else:
        dict[list[i]] = 1
print(dict)


