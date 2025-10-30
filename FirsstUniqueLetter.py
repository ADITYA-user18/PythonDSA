s = "leetcode"
dict = {}

for ch in s:
    if ch in dict:
        dict[ch] +=1
    else:
        dict[ch] =1

for i in range(0,len(s)):
    if dict[s[i]] == 1:
        print(s[i],i)
        break
else:
    print(-1)





    

