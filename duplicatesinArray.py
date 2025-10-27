list = [1,2,1,5,7,8,4,8,5]

dict = {}

new_list = []

for i in range(len(list)):
    if list[i] in dict:
        dict[list[i]] += 1
    else:
          dict[list[i]] = 1


for key in dict:
     if dict[key] > 1:
          new_list.append(key)
          
print(new_list)


