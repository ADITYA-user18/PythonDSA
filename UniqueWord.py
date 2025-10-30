s = "aabbc"

dict = {}

for i in range(0,len(str(s))):
    if s[i] not in dict:
        dict[s[i]] = 1
    else:
        dict[s[i]] += 1

for key in dict:
    if dict[key] == 1:
        print(key)
    