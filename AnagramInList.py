arr = ["eat","tea","tan","ate","nat","bat"]
dict={}

for i in range(0,len(arr)):
    key = "".join(sorted(arr[i]))

    if key not in dict:
        dict[key] = [arr[i]]
    else:
       dict[key].append(arr[i])
print(dict)

    
    